#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup, Command


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys
        import subprocess

        errno = subprocess.call([
            sys.executable, './tests/test_readitlater.py', ])
        raise SystemExit(errno)


setup(
    name='readitlater',
    version='0.1.1',
    author='Kosei Kitahara',
    author_email='surgo.jp@gmail.com',
    url='https://bitbucket.org/Surgo/ril/',
    download_url='https://bitbucket.org/Surgo/ril/downloads',
    description='Pocket (Formerly ReadItLater) library for Python.',
    cmdclass={
        'test': PyTest,
    },
    license='BSD',
    packages=[
        'readitlater',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
