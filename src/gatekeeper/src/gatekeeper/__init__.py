# -*- coding: utf-8 -*-

import logging
from zope.i18nmessageid import MessageFactory
from cromlech.i18n import Locale
from cromlech.webob.request import Request
from cromlech.browser import IView
from gk.login.interfaces import DirectResponse


def query_view(request, obj, name=""):
    return IView(obj, request, name=name)


SESSION_KEY = "gatekeeper.session"
i18n = MessageFactory("gatekeeper")
logger = logging.getLogger('gatekeeper')


def log(message, summary='', severity=logging.DEBUG):
    logger.log(severity, '%s %s', summary, message)


def serve_view(viewname, root=None, skin_layer=None):

    def app(environ, start_response):
        with Locale('de'):
            try:
                request = Request(environ)
                if skin_layer:
                    alsoProvides(request, skin_layer)
                form = query_view(request, root or environ, name=viewname)
                response = form()(environ, start_response)
            except DirectResponse as dr:
                print(dr)
                response = dr.response(environ, start_response)
        return response

    return app
