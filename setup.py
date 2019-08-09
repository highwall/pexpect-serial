# -*- coding: utf-8 -*-

import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='pexpect-serial',
    version='0.1.0',
    author='High Wall',
    author_email='hiwall@126.com',
    description='pexpect with pyserial',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/highwall/pexpect-serial',
    packages=setuptools.find_packages(exclude=('tests', 'docs')),
    install_requires=['pexpect', 'pyserial'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
