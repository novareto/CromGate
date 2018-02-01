from setuptools import setup, find_packages
import sys, os


version = '0.1'

setup(name='keeper',
      version=version,
      description="",
      long_description=""" """,
      classifiers=[],
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages('keeper'),
      package_dir = {'': 'keeper'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'fanstatic',
          'gatekeeper',
          'grokker',
          'dolmen.view',
          'dolmen.forms.base',
          'dolmen.forms.ztk',
      ],
      entry_points = {
          'fanstatic.libraries': [
              'keeper=keeper.resources:library',
          ],
      },
)
