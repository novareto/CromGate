# -*- coding: utf-8 -*-

from os.path import join
from setuptools import setup, find_packages

version = '0.1-dev'
readme = open('README.txt').read()
history = open(join('docs', 'HISTORY.txt')).read()

install_requires = [
    'cromlech.webob',
    'dolmen.forms.base',
    'dolmen.forms.ztk',
    'dolmen.location',
    'dolmen.tales',
    'dolmen.viewlet',
    'fanstatic',
    'gatekeeper',
    'gk.login',
    'js.bootstrap',
    'setuptools',
    'zope.i18nmessageid',
    'zope.interface',
    ]

tests_require = [
    'zope.testing',
    ]

setup(name='gk.layout',
      version=version,
      description="Gatekeeper layout",
      long_description="%s\n\n%s\n" % (readme, history),
      keywords='Gatekeeper Novareto',
      author='Novareto',
      author_email='',
      url='',
      license='',
      namespace_packages=['gk'],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require=dict(test=tests_require),
      classifiers=[
          'Environment :: Web Environment',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
          ],
      entry_points="""
      # -*- Entry points: -*-
      [fanstatic.libraries]
      gatekeeper = gk.layout.resources:library
      datepicker = gk.layout.resources:datepicker
      """,
      )
