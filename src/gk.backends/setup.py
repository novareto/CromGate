from setuptools import setup, find_packages
import os

readme_filename = os.path.join('src', 'gk', 'backends', 'README.txt')
long_description = open(readme_filename).read() + '\n\n' + \
                   open('CHANGES.txt').read()

test_requires = [
    ]

setup(name='gk.backends',
      version='1.0',
      description="Backends system for Gatekeeper",
      long_description = long_description,
      classifiers=['Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: Zope Public License',
                   'Programming Language :: Python',
                   'Framework :: Zope3',
                   ],
      keywords='backends gatekeeper',
      author='Novareto',
      author_email='grok-dev@zope.org',
      url='http://grok.zope.org',
      license='ZPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['gk'],
      include_package_data=True,
      zip_safe=False,
      extras_require={'test': test_requires},
      install_requires=[
          ],
      )
