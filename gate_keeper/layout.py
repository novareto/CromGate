# -*- coding: utf-8 -*-

import crom
from zope.interface import Interface
from gatekeeper.layout import Layout
from cromlech.browser import IRequest, ILayout
from .resources import gkcss
from . import tal_template


@crom.component
@crom.sources(IRequest, Interface)
@crom.target(ILayout)
class GKLayout(Layout):
    resources = [gkcss]
    template = tal_template('layout.pt')
