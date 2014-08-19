#-*- coding:utf-8 -*-
#
# Copyright (C) 2013 - Pranjal Mittal <pranjal.mittal.ece10@iitbhu.ac.in>
#
# Distributed under the BSD license, see LICENSE.txt


from setuptools import setup, find_packages
import sys, os

dependencies = ['requests', 'simplejson',]

setup(
    name='makemymails',
    version='0.0.1',
    description='Makemymails Sms: Add sms sending capability to your webisite using your android device.',
    long_description=open('README.rst').read(),
    packages=['makemymails',],
    license='BSD',
    keywords='sms gateway android api',
    author='Pranjal Mittal',
    install_requires=dependencies,
    author_email='pranjal@makemymails.com',
    classifiers=[
      "Intended Audience :: Developers",
      "Development Status :: 4 - Beta",
      "Programming Language :: Python :: 2",
    ],
    url='https://github.com/pramttl/makemymails-sms',
    include_package_data=True,
)


