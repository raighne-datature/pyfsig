#!/usr/bin/env python

from distutils.core import setup

def readme():
    with open('README.md', encoding='UTF8') as f:
        return f.read()

setup(name='pyfsig',
      version='0.8.3',
      description='A python library for identifying files by headers (magic bytes)',
      long_description=readme(),
      author='schlerp',
      author_email='schlerpderpson@gmail.com',
      url='https://github.com/schlerp/pyfsig',
      packages=['pyfsig'],
      package_dir={'pyfsig': 'src/pyfsig'},
      classifiers=['Operating System :: MacOS :: MacOS X',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX',
                   'Programming Language :: Python',
                   ],
      )
