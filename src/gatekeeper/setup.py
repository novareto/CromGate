from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='gatekeeper',
      version=version,
      description="",
      long_description=""" """,
      classifiers=[],
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "dolmen.tales",
          "pycryptodome",
          "cromlech.browser",
          "cromlech.dawnlight",
          "cromlech.webob",
          "dolmen.template",
          "dolmen.view",
          "js.bootstrap",
          "setuptools",
          "wsgistate",
          "gk.login",
          "gk.layout",
          "gk.crypto",
      ],
)
