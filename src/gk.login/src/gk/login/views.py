# -*- coding: utf-8 -*-

from os import path
from cromlech.browser import IPublicationRoot
from dolmen.view import name, context, view_component
from dolmen.template import TALTemplate
from dolmen.view import View, make_layout_response
from cromlech.webob import Response


TEMPLATE_DIR = path.join(path.dirname(__file__), 'templates')


def tal_template(name):
    return TALTemplate(path.join(TEMPLATE_DIR, name))


timeout_template = tal_template('timeout.pt')
unauthorized_template = tal_template('unauthorized.pt')


@view_component
@name('unauthorized')
@context(IPublicationRoot)
class Unauthorized(View):
    template = unauthorized_template
    responseFactory = Response
