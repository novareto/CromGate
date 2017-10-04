# -*- coding: utf-8 -*-

import logging
from zope.i18nmessageid import MessageFactory
from cromlech.i18n import Locale
from cromlech.browser import setSession
from cromlech.webob.request import Request
from cromlech.browser import IView
from cromlech.wsgistate import WsgistateSession


def query_view(request, obj, name=""):
    return IView(obj, request, name=name)


SESSION_KEY = "gatekeeper.session"
i18n = MessageFactory("gatekeeper")
logger = logging.getLogger('gatekeeper')


def log(message, summary='', severity=logging.DEBUG):
    logger.log(severity, '%s %s', summary, message)


def serve_view(viewname, root=None, session_key=SESSION_KEY, skin_layer=None):

    def app(environ, start_response):
        with Locale('de'):
            with WsgistateSession(environ, session_key):
                request = Request(environ)
                if skin_layer:
                    alsoProvides(request, skin_layer)
                form = query_view(request, root or environ, name=viewname)
                response = form()(environ, start_response)
                setSession()
        return response

    return app
