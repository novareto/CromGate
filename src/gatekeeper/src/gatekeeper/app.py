# -*- coding: utf-8 -*-


from cromlech.browser import IPublicationRoot
from zope.interface import implementer
from zope.location import Location


@implementer(IPublicationRoot)
class GateKeeper(Location):

    def get_portals(self, request):
        user = request.environment['REMOTE_USER']
        tokens = request.environment['REMOTE_ACCESS']
