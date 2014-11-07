#!/usr/bin/python
from distutils.core import setup
import os

setup(name='Steganocrypto',
      version='0.0.3',
      description='Python image steganography',
      author='Gabriel Ribeiro',
      author_email='gabrielrdavid@gmail.com',
      url='https://github.com/gabrielhribeiro/Steganocrypto',
      license='GPL',
      py_modules=['Steganocrypto','aes','stepic'],
      scripts=['Steganocrypto','aes','stepic'],
      data_files=[('Steganocrypto', []),
                  ('aes', [])],
      classifiers=[
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Environment :: Console',
          'Topic :: Multimedia :: Graphics',
          'Topic :: Utilities',
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python' #duh!
          ]
      )
