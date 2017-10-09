# -*- coding: utf-8 -*-


from cromlech.browser import IView, IPublicationRoot
from cromlech.webob.request import Request

from zope.interface import alsoProvides, implementer
from zope.location import Location

from gk.layout import DefaultLayer
from gk.crypto import ticket as tlib
from . import query_view


@implementer(IPublicationRoot)
class GateKeeper(Location):

    def get_portals(self, request):
        user = request.environment['REMOTE_USER']
        tokens = request.environment['REMOTE_ACCESS']


class Keeper(object):

    def __init__(self, pubkey):
        self.site = GateKeeper()
        self.pubkey = pubkey

    def __call__(self, environ, start_response):

        @tlib.signed_cookie(self.pubkey)
        def publish(request, root):
            view = query_view(request, root, name=u'index')
            if view is not None:
                return view
            return query_view(request, root, name=u'notfound')

        # Layer
        request = Request(environ)
        alsoProvides(request, DefaultLayer)

        view, error = publish(request, self.site)
        if error is not None:
            view = query_view(request, self.site, name='unauthorized')

        response = view()
        return response(environ, start_response)
