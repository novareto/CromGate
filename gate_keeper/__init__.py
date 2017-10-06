# -*- coding: utf-8 -*-

from os import path
from zope.i18nmessageid import MessageFactory
from cromlech.webob import Response
from cromlech.browser.interfaces import ITypedRequest
from dolmen.template import TALTemplate
from dolmen.view import View, make_layout_response


i18n = MessageFactory("gk.layout")
TEMPLATE_DIR = path.join(path.dirname(__file__), 'templates')


def tal_template(name):
    return TALTemplate(path.join(TEMPLATE_DIR, name))


class Page(View):
    responseFactory = Response
    make_response = make_layout_response


class DefaultLayer(ITypedRequest):
    pass
