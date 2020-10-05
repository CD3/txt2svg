#! /usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='txt2svg',
    license="MIT",
    version="0.1",
    description='A tool for generating svg images from plain text files.',
    url='https://github.com/CD3/txt2svg',
    author='C.D. Clark III',
    packages=find_packages(),
    install_requires=['click','lxml'],
    entry_points='''
    [console_scripts]
    txt2svg=txt2svg.scripts.txt2svg:main
    ''',
)
