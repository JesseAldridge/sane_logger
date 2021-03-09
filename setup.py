from setuptools import setup, find_packages
import sys, os

version = '0.0.4'

setup(name='sane_logger',
      version=version,
      description="My preferred logger config.",
      long_description="""""",
      classifiers=[],
      keywords='logging',
      author='Jesse Aldridge',
      author_email='JesseAldridge@gmail.com',
      url='https://github.com/JesseAldridge/sane_logger',
      license='MIT',
      packages=['sane_logger'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ]
      )
