# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


readme = '''Introduction
------------

This is like pexpect, but it will work with serial port that you
pass it. You are reponsible for opening and close the serial port.
This allows you to use Pexpect with Serial port which pyserial supports.

Usage
-----

sample code::

    import serial
    from pexpect_serial import SerialSpawn
    ser = serial.Serial('COM1', 115200)
    ss = SerialSpawn(ser)
    ss.sendline('start')
    ss.expect('done')

License
-------
MIT'''

license = '''The MIT License (MIT)

Copyright (c) 2016 highwall

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

setup(
    name='pexpect-serial',
    version='0.0.4',
    description='pexpect with pyserial',
    long_description=readme,
    author='High Wall',
    author_email='hiwall@126.com',
    url='https://github.com/highwall/pexpect-serial',
    license=license,
    package_data={
        '': ['README.md', 'LICENSE']
    },
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'pexpect'
    ],
)
