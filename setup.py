#!/usr/bin/env python
#
# =====================================================================================
#
#       Filename:  setup.py
#
#    Description:  setup file for sampler utilities
#
#        Created:  28/03/2017 11:43:22
#
#         Author:  Sergio Orlandini (SO), s.orlandini@cineca.it
#   Organization:  CINECA
#
# =====================================================================================
#

from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()
    
setup(
    name='DHT22',
    version='1.0',
    description='A useful module',
    license="MIT",
    long_description=long_description,
    author='Man Foo',
    author_email='foomail@foo.com',
    url="http://www.foopackage.com/",
    packages=['DHT22'],  #same as name
    #install_requires=['pandas', 'numpy'], #external packages as dependencies
    #scripts=[
    #    'bin/dht22-db',
    #]
    entry_points={  # Optional
        'console_scripts': [
        'run = DHT22.__main__:main'
        ],
    },
    
)
