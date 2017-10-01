# -*- coding: utf-8 -*-

from os import chmod, path, makedirs
from loader import Configuration


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
            fd.write(pubkey.exportKey('OpenSSH'))


with Configuration('config.json') as config:
    from crom.config import configure
    from cromlech.sqlalchemy import create_engine
    from gatekeeper.app import Keeper
    from gk.admin import Admin

    # Generate the key pair
    create_rsa_pair(config['crypto']['privkey'], config['crypto']['pubkey'])

    # Dependencies, ZCML free.
    import crom
    import gk.login
    import grokker, dolmen.view, dolmen.forms.base, dolmen.forms.ztk
    from dolmen.forms.ztk.fields import registerDefault

    crom.monkey.incompat()
    crom.implicit.initialize()
    registerDefault()

    configure(
        grokker,
        dolmen.view,
        dolmen.forms.base,
        dolmen.forms.ztk,
        gk.login,
    )

    portals = config.get('portals')
    if portals is not None:
        pass  # FIX ME

    # Configuring the SQL Connector
    engine = create_engine(config['db']['uri'], "admin")
    engine.bind(Admin)

    # The application.
    application = Keeper(engine, config['crypto']['pubkey']).publisher
