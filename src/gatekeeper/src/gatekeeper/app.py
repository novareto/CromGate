# -*- coding: utf-8 -*-


from cromlech.browser import exceptions, setSession, IView
from cromlech.webob.request import Request
from cromlech.sqlalchemy import SQLAlchemySession

from zope.interface import alsoProvides, implementer
from zope.location import Location

from gk.crypto import ticket as tlib
from gk.backends import IPortal, XMLRPCPortal
from gk.admin import Admin, get_valid_messages, styles


def query_view(request, obj, name=""):
    return IView(obj, request, name=name)


@implementer(IRootObject)
class GateKeeper(Location):

    def __init__(self, engine):
        self.engine = engine

    def get_portals(self, request):
        user = request.environment['REMOTE_USER']
        tokens = request.environment['REMOTE_ACCESS']
        for name in tokens:
            gateway = IPortal.component(name=name)
            yield {
                "title": gateway.title,
                "url": gateway.backurl,
                "dashboard": gateway.get_dashboard(user),
                }

    def get_messages(self):
        with SQLAlchemySession(self.engine) as session:
            messages = [
                {'msg': m.message, 'type': m.type, 'style': styles[m.type]}
                for m in get_valid_messages(session)]
        return messages


class Keeper(object):

    def __init__(self, engine):
        self.site = GateKeeper(engine)
        
    def publisher(environ, start_response):

        @tlib.signed_cookie(pubkey)
        def publish(request, root):
            view = query_view(request, self.site, name=u'index')
            if view is not None:
                return view
            return query_view(request, self.site, name=u'notfound')

        request = Request(environ)
        if layer is not None:
            skin_layer = eval_loader(layer)
            alsoProvides(request, skin_layer)

        view, error = publish(request, site)
        if error is not None:
            view = query_view(request, site, name=u'unauthorized')
            view.set_message(error.title)
        response = view()

        return response(environ, start_response)
    return publisher
