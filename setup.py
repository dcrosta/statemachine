from distribute_setup import use_setuptools
use_setuptools('0.6c15')

from setuptools import setup

setup(name='statemachine',
      version='0.1',
      description='Simple Finite-State Machines',
      author='Kyle Conroy',
      author_email='kyle@kyleconroy.com',
      url='https://github.com/kyleconroy/statemachine',
      py_modules=['statemachine'],
     )
