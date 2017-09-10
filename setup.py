from setuptools import setup
from allianceauth_api import __version__


setup(name='allianceauth-api',
      version=__version__,
      description='OpenAPI for AllianceAuth',
      url='https://github.com/basraah/allianceauth-api',
      author='Basraah',
      author_email='basraaheve@gmail.com',
      license='AGPL-3.0',
      packages=['allianceauth_api'],
      install_requires=[
          'djangorestframework>=3.6.2',
          'django-rest-swagger>=2.1.2',
      ],
      zip_safe=False,
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Affero General Public License v3',
          'Natural Language :: English',
          'Programming Language :: Python :: 3.5',
          'Framework :: Django :: 1.10',
          'Framework :: Django :: 1.11',
      ],
      )
