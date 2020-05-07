# coding=utf-8

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(name='API Tinder',
      version='2020.5',
      description='Tinder API for Python',
      long_description=readme,
      author='Filipe Rocha',
      #author_email='',
      url='https://github.com/filiperochs/api-tinder',
      py_modules=['api', 'api_min', 'auth_fb', 'auth_tinder'],
      install_requires=['requests',
                        'robobrowser',
                        'lxml'],
      license=license,
      zip_safe=False,
      keywords=['tinder-api', 'tinder', 'python-3', 'robobrowser'],
      packages=find_packages()
      #classifiers=[]
     )
