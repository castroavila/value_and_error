#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <manuel.castro@inpe.br>
# @file             : functions.py	
# @created          : 16-Feb-2019
# @company          : National Institute for Space Research (INPE) - São José dos Campos/SP - Brazil
# 

'''

  This script has been developed under financial support from FAPESP (Fundação  
  de Amparo à Pesquisa do Estado de São Paulo, Brazil) under grant #2015/25972-0

 The code is based on the remeis isisscript's function TeX_value_pm_error. The    
 scripts can be found at http://www.sternwarte.uni-erlangen.de/isis/              
'''


'''
This fuinction computes the first significant figure's position from the error.

It is expected that a real measurement be expressed as: LowLimit < ExpectedValue
< HighLimit. So the first significant figure's positon is calcaluted from either
ExpectedValue - LowLimit or HighLimit - ExpectedValue , depending on which has
the highest amount of leading zeros.

Code intended to run under Python 3 or above 

'''

from math import *

'''
x is either low_error = ExpectedValue - LowLimit  or high_error = HighLimit - ExpectedValue. 
digits stores the position of the first significant figure. Since the first
significant figure's position in low_error and high_error couldn't be the same.
In such a case digit equals to the highest position.
'''
def significant_figure(x):
    digits = floor(log10(x))
    #accounts for numerical problems  
    x = round(x*pow(10,-digits))*pow(10,digits)
    digits = floor(log10(x))
    
    #check if the leading digit in the uncertainty is 1, like 0.01243, 0.0123. 
    # in such a case the uncertainty retains two significant figures

    if (digits <0):
        value =  float (fmt(digits).format(x))
        if ( (value/(1.*pow(10,digits))) <= 1. ):
            digits-=1

    return digits

    #Set the proper output formatting taking into account the number of significant figures.

def fmt(ndigits):
    if (ndigits < 0):

        formatting = "{0:"+  "0.{0:1d}f".format(int(-ndigits)) + "}"
    else:

        formatting = "{0:"+  "{0:1d}d".format(int(ndigits)) + "}"

    return formatting

