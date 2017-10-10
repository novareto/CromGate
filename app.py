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


with Configuration('etc/config.json') as config:

    # Generate the key pair
    create_rsa_pair(config['crypto']['privkey'], config['crypto']['pubkey'])

    # Dependencies, ZCML free.
    import crom
    import dolmen.tales
    import gatekeeper
    import gk.login
    import gate_keeper
    import grokker, dolmen.view, dolmen.forms.base, dolmen.forms.ztk
    from dolmen.forms.ztk.fields import registerDefault
    from fanstatic import Fanstatic
    from gk.crypto.ticket import cipher
    
    crom.monkey.incompat()
    crom.implicit.initialize()
    registerDefault()

    crom.configure(
        dolmen.tales,
        dolmen.forms.base,
        dolmen.forms.ztk,
        dolmen.view,
        gatekeeper,
        gate_keeper,
        gk.login,
        grokker,
    )

    from gatekeeper import serve_view
    #from gatekeeper.app import Keeper
    from gk.login.models import LoginRoot
    from rutter.urlmap import URLMap

    class LoginRoot(LoginRoot):

        def __init__(self, pubkey, dest):
            self.pkey = pubkey
            self.dest = dest

    # Login
    loginroot = LoginRoot(
        config['crypto']['pubkey'],
        config['global']['dest'],
    )

    # The application.
    mapping = URLMap()
    # mapping['/'] = Keeper(config['crypto']['pubkey'])
    mapping['/'] = cipher(serve_view(
        'login', root=loginroot), None, config['crypto']['cipher'])
    mapping['/'] = serve_view('login', root=loginroot)
    mapping['/unauthorized'] = serve_view('unauthorized', root=loginroot)
    mapping['/timeout'] = serve_view('timeout', root=loginroot)

    # Middlewares wrapping
    application = Fanstatic(mapping)

    print(application, "Application is ready.")
