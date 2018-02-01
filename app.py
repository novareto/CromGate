#!./bin/python3.4
# -*- coding: utf-8 -*-

from os import chmod, path, makedirs
#from loader import Configuration

import os
import sys
import json


CH_DIR = os.path.abspath(os.path.dirname(__file__))


class Configuration(object):

    def __init__(self, filename, directory=CH_DIR):
        env = os.path.join(directory, filename)
        if not os.path.isfile(env):
            raise RuntimeError('Configuration file does not exist.')
        self.environ = env
        self.backup = sys.path[:]

    def __enter__(self):
        with open(self.environ, "r") as fd:
            env = json.load(fd)

        paths = env['paths']
        sys.path[0:0] = paths
        return env['conf']

    def __exit__(self, exc_type, exc_val, exc_tb):
        # we need to make something about error handling.
        sys.path = self.backup


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
    # create_rsa_pair(config['crypto']['privkey'], config['crypto']['pubkey'])

    # Dependencies, ZCML free.
    import crom
    import dolmen.tales
    import gatekeeper
    import keeper
    import grokker, dolmen.view, dolmen.forms.base, dolmen.forms.ztk
    from dolmen.forms.ztk.fields import registerDefault
    from gatekeeper.ticket import cipher

    crom.monkey.incompat()
    crom.implicit.initialize()
    registerDefault()

    crom.configure(
        dolmen.forms.base,
        dolmen.forms.ztk,
        dolmen.tales,
        dolmen.view,
        keeper,
        gatekeeper,
        grokker,
    )

    from gatekeeper import serve_view
    from gatekeeper.login.models import LoginRoot
    from rutter.urlmap import URLMap

    class LoginRoot(LoginRoot):

        def __init__(self, pubkey, dest):
            self.pkey = pubkey
            self.dest = dest

    # Login
    loginroot = LoginRoot(
        config['crypto']['privkey'],
        config['global']['dest'],
    )

    # The application.
    mapping = URLMap()
    mapping['/'] = cipher(serve_view(
        'login', root=loginroot), None, config['crypto']['cipher'])
    mapping['/unauthorized'] = serve_view('unauthorized', root=loginroot)
    mapping['/timeout'] = serve_view('timeout', root=loginroot)

    # Middlewares wrapping if needed
    application = mapping

    print(application, "Application is ready.")
