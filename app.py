# -*- coding: utf-8 -*-

from loader import Configuration


with Configuration('config.json') as config:
    from crom.config import configure
    from cromlech.sqlalchemy import create_engine
    from gatekeeper.app import keeper
    from gk.admin import Admin,

    # Dependencies, ZCML free.
    configure(
        'grokker',
        'dolmen.view',
        'dolmen.forms.base',
        'dolmen.forms.ztk',
    )

    portals = config.get('portals')
    if portals is not None:
        pass  # FIX ME


    # Configuring the SQL Connector
    engine = create_engine(config['db']['uri'], "admin")
    engine.bind(Admin)

    
    site = GateKeeper(engine)

