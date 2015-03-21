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
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',	
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Topic :: Communications :: Email',
		  'Topic :: Education',
		  'Topic :: Software Development :: Libraries :: Python Modules',
          ],
      license="GNU GENERAL PUBLIC LICENSE"
     )

