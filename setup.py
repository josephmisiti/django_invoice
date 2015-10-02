#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import dj_invoice

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = dj_invoice.__version__

# if sys.argv[-1] == 'publish':
#     os.system('python setup.py sdist upload')
#     os.system('python setup.py bdist_wheel upload')
#     sys.exit()
#
# if sys.argv[-1] == 'tag':
#     print("Tagging the version on github:")
#     os.system("git tag -a %s -m 'version %s'" % (version, version))
#     os.system("git push --tags")
#     sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

INSTALL_REQUIRES = [
    'django>=1.6',
    'pypdf2',
]

setup(
    name='django_invoice',
    version=version,
    description="""An simple invoicing tool for Django""",
    long_description=readme + '\n\n' + history,
    author='Joseph Misiti',
    author_email='joseph.misiti@gmail.com',
    url='https://github.com/josephmisiti/django_invoice',
    packages=[
        'dj_invoice',
    ],
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    license="BSD",
    zip_safe=False,
    keywords='django_invoice',
    classifiers=[
        'Development Status :: `` - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)