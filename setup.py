#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import find_packages, setup

__version__ = 1.0.0

REPO_URL = "https://github.com/SSJenny90/geoage-calculator"

README = ''
for ext in ['md','rst']:
    try:
        with open(os.path.join(os.path.dirname(__file__), 'README.' + ext)) as readme:
            README = readme.read()
    except FileNotFoundError as fnfe:
        pass


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='geoage-calculator',
    version=__version__,
    author='Sam Jennings',
    license='MIT',
    description='Simple functions for dealing with datasets that contain incosistently formatted geological age data.',
    long_description=README,
    url=REPO_URL,
    download_url=REPO_URL + 'releases/tag/v' + __version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    zip_safe=False,
    keywords='scientific geology geochronology stratigraphy',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
