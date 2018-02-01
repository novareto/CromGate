# -*- coding: utf-8 -*-

from cromlech.browser.interfaces import IURL
from cromlech.webob import Response
from dolmen.forms.base import name, context, form_component
from dolmen.view import make_layout_response
from gatekeeper.login.form import BaseLoginForm
from gatekeeper.login.models import LoginRoot
from . import tal_template


@form_component
@name('login')
@context(LoginRoot)
class Login(BaseLoginForm):
    responseFactory = Response
    make_response = make_layout_response
    template = tal_template('form.pt')

    def back(self, login):
        return "https://testasd.kuvb.de"

    @property
    def action_url(self):
        url = IURL(self.context, self.request, default=None)
        return url

    def authenticate(self, login, password):
        print ('HANS PETER KALUS')
        if login == "0101010001" and password == "passwort":
            return ['testasd.kuvb.de', ]
        return []
