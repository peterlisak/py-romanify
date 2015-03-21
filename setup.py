#!/usr/bin/env python

from distutils.core import setup

with open('README') as file:
    long_description = file.read()

setup(name='py-romanify',
      version='0.1.0',
      description='Python Roman/Arabic numerals convertor',
      long_description=long_description,
      author='Peter Lisak',
      author_email='peter.lisak+pypi@gmail.com',
      url='https://github.com/peter-lisak/py-romanify',
      packages=['romanify'],
      license="GNU GENERAL PUBLIC LICENSE"
     )

# check long-desc
#python setup.py --long-description | rst2html.py > output.html