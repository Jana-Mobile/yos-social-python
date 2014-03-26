#!/usr/bin/python

__author__ = 'Dustin Whittle <dustin@yahoo-inc.com>'

from distutils.core import setup

setup(
    name='yos_social_sdk',
    version='0.0.5',
    description='Python client library for Yahoo! Social + Data REST APIs',
    author='Dustin Whittle',
    author_email='dustin@yahoo-inc.com',
    license='MIT',
    url='http://github.com/yahoo/yos-social-python/tree/master',
    packages=['yahoo','yahoo.oauthlib'],
    package_dir={'yahoo': 'src/yahoo'},
    install_requires=[
        'simplejson >= 1.3',
        'python-openid >= 2.2.1'
    ]
)
