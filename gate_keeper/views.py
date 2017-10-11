# -*- coding: utf-8 -*-

from gk.login.form import BaseLoginForm
from gk.login.models import LoginRoot
from dolmen.forms.base import name, context, form_component
from cromlech.webob import Response
from cromlech.browser import request, IPublicationRoot
from dolmen.view import view_component
from gatekeeper.app import GateKeeper
from gk.layout import DefaultLayer, Page
from . import tal_template
from .resources import gkcss
from dolmen.view import make_layout_response
from cromlech.browser.interfaces import IURL


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
        return False


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
