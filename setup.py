from setuptools import setup, find_packages
import sys, os


version = '0.1'

setup(name='gate_keeper',
      version=version,
      description="",
      long_description=""" """,
      classifiers=[],
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages('gate_keeper'),
      package_dir = {'': 'gate_keeper'},
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
              'gate_keeper=gate_keeper.resources:library',
          ],
      },
)
