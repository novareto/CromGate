# -*- coding: utf-8 -*-

from gk.login.form import BaseLoginForm
from gk.login.models import LoginRoot
from dolmen.forms.base import name, context, form_component
from dolmen.forms.base import Fields, Action, Actions, FAILURE
from cromlech.webob import Response


@form_component
@name('login')
@context(LoginRoot)
class Login(BaseLoginForm):
    responseFactory = Response
