# -*- coding: utf-8 -*-

from fanstatic import Library, Resource


library = Library('gate_keeper', 'static')
gkcss = Resource(library, 'gk.css', depends=[])
gkcss.dependency_nr = 1
