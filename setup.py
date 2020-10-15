#!/usr/bin/env python 
# forked from https://github.com/countercept/python-exe-unpacker
from setuptools import setup

entry_points = {
    'console_scripts': [
        ['python_exe_unpack=python_exe_unpack.python_exe_unpack:main']
    ]
}

setup(
    name='python-exe-unpacker',
    version='1.0',
    packages=[
        'python_exe_unpack'
    ],
    url='https://github.com/countercept/python-exe-unpacker',
    license='GNU General Public License',
    author='In Ming Loh (@tantaryu) ',
    author_email='inming.loh@countercept.com',
    long_description=open('README.md').read(),
    entry_points=entry_points,
    install_requires=[
        'pefile==2017.9.3',
        'unpy2exe==0.3',
        'uncompyle6==2.11.5',
        'xdis==3.5.5',
        'pycrypto==2.6.1',
        'configparser==3.5.0'
    ],
    # include_package_data=True
)
# ~nuninuninu~
