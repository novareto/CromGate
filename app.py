# -*- coding: utf-8 -*-

from os import chmod, path, makedirs
from loader import Configuration


SESSION_KEY = "gatekeeper.session"


def create_rsa_pair(pvt_path, pub_path):
    from Crypto.PublicKey import RSA

    priv = path.isfile(pvt_path)
    pub = path.isfile(pub_path)

    if not priv or not pub:  # IMPORTANT : We override the existing one.

        container = path.dirname(pvt_path)
        if not path.isdir(container):
            makedirs(container)

        container = path.dirname(pub_path)
        if not path.isdir(container):
            makedirs(container)
            
        key = RSA.generate(2048)

        with open(pvt_path, 'wb') as fd:
            chmod(pvt_path, 0o600)
            fd.write(key.exportKey('PEM'))

        pubkey = key.publickey()
        with open(pub_path, 'wb') as fd:
            fd.write(pubkey.exportKey('PEM'))


with Configuration('config.json') as config:
    from cromlech.sqlalchemy import create_engine
    from cromlech.wsgistate.middleware import file_session
    from gatekeeper import serve_view
    from gatekeeper.app import Keeper
    from gk.admin import Admin
    from gk.login.models import LoginRoot
    from rutter.urlmap import URLMap
    
    # Generate the key pair
    create_rsa_pair(config['crypto']['privkey'], config['crypto']['pubkey'])

    # Dependencies, ZCML free.
    import crom
    import gatekeeper
    import gk.login
    import grokker, dolmen.view, dolmen.forms.base, dolmen.forms.ztk
    from dolmen.forms.ztk.fields import registerDefault
    from dolmen.collection import load
    
    crom.monkey.incompat()
    crom.implicit.initialize()
    registerDefault()

    crom.configure(
        grokker,
        dolmen.view,
        dolmen.forms.base,
        dolmen.forms.ztk,
        gk.login,
        gatekeeper,
    )

    load.loadComponents()
    
    # Configuring the SQL Connector
    engine = create_engine(config['db']['uri'], "admin")
    engine.bind(Admin)
    
    # Login
    loginroot = LoginRoot()

    # Session configuration
    session_key = config['session'].get('key', SESSION_KEY)
    session_path = config['session'].get('path', '/tmp')
    session_timeout = config['session'].get('timeout', 300)
    session_wrapper = file_session(
        session_path, key=session_key, timeout=session_timeout)
    
    # The application.
    mapping = URLMap()
    mapping['/'] = Keeper(engine, config['crypto']['pubkey']).publisher
    mapping['/login'] = serve_view(
        'login', root=loginroot, session_key=session_key)
    mapping['/unauthorized'] = serve_view(
        'unauthorized', session_key=session_key)
    mapping['/timeout'] = serve_view(
        'timeout', session_key=session_key)

    # Session wrapping
    application = session_wrapper(mapping)
