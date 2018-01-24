# -*- coding: utf-8 -*-

from cromlech.browser import request, IPublicationRoot
from cromlech.browser.interfaces import IURL
from cromlech.webob import Response
from dolmen.forms.base import name, context, form_component
from dolmen.view import make_layout_response, view_component
from gatekeeper import DefaultLayer, Page
from gatekeeper.app import GateKeeper
from gatekeeper.login.form import BaseLoginForm
from gatekeeper.login.models import LoginRoot

from . import tal_template
from .resources import gkcss


@form_component
@name('login')
@context(LoginRoot)
class Login(BaseLoginForm):
    responseFactory = Response
    make_response = make_layout_response

    @property
    def action_url(self):
        url = IURL(self.context, self.request, default=None)
        return url

    def update(self):
        gkcss.need()

    def authenticate(self, login, password):
        if login == "0101010001" and password == "passwort":
            return ['test.siguv.de', ]
        return []


@view_component
@name('timeout')
@context(IPublicationRoot)
#@request(DefaultLayer)
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
@context(IPublicationRoot)
@request(DefaultLayer)
class Index(Page):

    def render(self):
        return "FIX ME"
