# -*- coding: utf-8 -*-

from os.path import join
from fanstatic import Library, Resource
from js.bootstrap import bootstrap

library = Library('gatekeeper', 'static')
styles = Resource(library, 'gk.css', depends=[bootstrap])

datepicker = Library('datepicker', join('static', 'datetime_picker'))
moment = Resource(
    datepicker, 'moment.js')
datepjs = Resource(
    datepicker, 'bootstrap-datetimepicker.min.js', depends=[bootstrap, moment])
datepcss = Resource(
    datepicker, 'bootstrap-datetimepicker.min.css')

gkdate = Resource(
    datepicker, 'gk.js', depends=[datepjs, datepcss])
