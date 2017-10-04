# -*- coding: utf-8 -*-

from cromlech.browser import request, IPublicationRoot
from cromlech.webob import Response
from dolmen.forms.base import Actions, Action
from dolmen.forms.base import DISPLAY, SuccessMarker
from dolmen.location import get_absolute_url
from dolmen.message.utils import send
from dolmen.view import name, context, view_component
from dolmen.forms.base import form_component
from gatekeeper.app import GateKeeper
from zope.interface import Interface
from . import i18n as _, DefaultLayer, tal_template, Page


@view_component
@name('timeout')
@context(IPublicationRoot)
@request(DefaultLayer)
class Timeout(Page):

    template = tal_template('timeout.pt')


@view_component
@name('unauthorized')
@context(IPublicationRoot)
@request(DefaultLayer)
class Unauthorized(Page):

    template = tal_template('unauthorized.pt')


@view_component
@name('notfound')
@context(IPublicationRoot)
@request(DefaultLayer)
class NotFound(Page):

    template = tal_template('404.pt')


@view_component
@name('index')
@context(GateKeeper)
@request(DefaultLayer)
class GatekeeperIndex(Page):

    def render(self):
        return "FIX ME"
