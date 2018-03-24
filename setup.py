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

with open("README.md", 'r') as f:
    long_description = f.read()
    
setup(
    name='DHT22',
    version='0.0.1',
    description='A useful module for DHT22 sensor',
    long_description=long_description,
    author='Davide Maggi',
    author_email='davide.maggi@tiscali.it',
    url="http://dmaggi.ddns.net",
    packages=['DHT22'],  #same as name
    install_requires=['pandas', 'numpy'], #external packages as dependencies
    #scripts=[
    #    'bin/dht22-db',
    #]
    entry_points={  # Optional
        'console_scripts': [
        'run = DHT22.__main__:main'
        ],
    },
    
)
