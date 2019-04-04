#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <manuel.castro@inpe.br>
# @file             : setup.py	
# @created          : 20-Mar-2019
# @company          : National Institute for Space Research (INPE)- São José dos Campos/SP - Brazil
# 

"""

"""

from distutils.core import setup 
#from setuptools import setup, find_packages
setup(
        name='value_and_error',
        version='1.0',
        description='Modules to proper error rounding and report uncertainties into LaTeX syntax',
        author='Manuel Castro',
        author_email='manuel.castro@inpe.br',
        url='www.',
        packages=['value_and_error','value_and_error.functions'],
#        py_modules=['functions']
        )
