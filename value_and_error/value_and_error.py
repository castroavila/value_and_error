#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <manuel.castro@inpe.br>
# @file             : value_and_error.py	
# @created          : 16-Feb-2019
# @company          : National Institute for Space Research (INPE) - São José dos Campos/SP - Brazil
# 

'''

  This script has been developed under financial support from FAPESP (Fundação  #
  de Amparo à Pesquisa do Estado de São Paulo, Brazil) under grant #2015/25972-0#

'''

'''
This script follows the theory giving in:
An introduction to error analysis: The study of uncertainties in physical
measurements, 2nd edition, John R.  Taylor, chapter 2, 1997.
'''


#import functions for significant figures and formatting
from .functions.functions import *


'''
A measurement is expressed as: 
LowLimit < ExpectedValue < HighLimit
'''
class value_and_error:
     
    def __init__(self,LowLimit, ExpectedValue, HighLimit):
        self.LowLimit = LowLimit
        self.ExpectedValue = ExpectedValue
        self.HighLimit = HighLimit
#        self.string=''
        if ( self.LowLimit < 0 or self.ExpectedValue < 0 or self.HighLimit < 0 ):
            print("Range values should be greater than 0")
            return 
            

    #Check that the values are as expected

        if (self.LowLimit < self.ExpectedValue):
            pass
        else:    
            print("Error: Low Value >= ExpectedValue")
            return 
        
        if(self.ExpectedValue < self.HighLimit):
            pass
        else:
            print("Error: ExpectedValue >= HighLimit")
            return

        self.LowError = self.ExpectedValue - self.LowLimit   
        self.HighError = self.HighLimit - self.ExpectedValue
#
#        scale = floor(log10(self.LowError))
#        self.mn = self.LowError*pow(10,-scale)*pow(10,scale)
#
#        scale = floor(log10(self.ExpectedValue))
#        self.value = self.ExpectedValue*pow(10,-scale)*pow(10,scale)
#    
#        scale = floor(log10(self.HighError))
#        self.mx = self.HighError*pow(10,-scale)*pow(10,scale)

        self.value = self.ExpectedValue
        self.mn = self.LowError
        self.mx = self.HighError

#        print('mn: {}'.format(self.mn))
#        print('mx: {}'.format(self.mx))

# # of digits


        digit1 = significant_figure(self.mn) 
        digit2 = significant_figure(self.mx)
        digits = min(digit1,digit2) 

#        print('digits: ')
#        print(digits)
    #check if the numbers must be expressed in scientific notation
        power=0
        if (0.001 <= self.HighError <= 100.):
            pass
        else:
            magnitude_order_value = significant_figure(self.value)
            power=max(magnitude_order_value,digits)
            self.value /= pow(10,power)
            self.mn /= pow(10,power)
            self.mx /= pow(10,power)

            #compute over significant figure
            digit1 = significant_figure(self.mn) 
            digit2 = significant_figure(self.mx)
            digits = min(digit1,digit2) 
        
#        print(fmt(digits))




    #Proper formatting
#        global string
        if(digits < 0):

            self.LowError = fmt(digits).format(self.mn)
            self.HighError = fmt(digits).format(self.mx)
            self.ExpectedValue = fmt(digits).format(self.value) 
    #generate proper LaTeX string
            if ( power == 0 ):

                if(float(self.LowError) == float(self.HighError)):
                    self.string='$' + self.ExpectedValue + '\\pm' +  self.LowError + '$' 

                if(float(self.LowError) != float(self.HighError)):
                    self.string='$' + self.ExpectedValue + '_{-' + self.LowError + '}^{+' + self.HighError + '}$'
            else:
            #in case of scientific notation             
                if(float(self.LowError) == float(self.HighError) ) :
                    self.string='$\\left(' + self.ExpectedValue + '\\pm' +  self.LowError + '\\right)\\times10^{' + str(power) + '}$' 

                if(float(self.LowError) != float(self.HighError) ):
                    self.string='$\\left(' + self.ExpectedValue + '_{-' + self.LowError + '}^{+' + self.HighError + '}\\right)\\times10^{'+str(power)+'}$'
             
        
        else:
            self.LowError = fmt(digits).format(int(round(self.mn)))
            self.HighError = fmt(digits).format(int(round(self.mx)))
            self.ExpectedValue = fmt(digits).format(int(round(self.value)))

    #generate proper LaTeX string

    # These lines should deal with expressions like
    # 92.81 \pm 3 ==> 93 \pm 3
    # 92.81 \pm 30  ==> 90 \pm 30
    # ....
            order = int(round(self.value)/pow(10,digits))
            self.value = pow(10, digits)*order
            self.ExpectedValue = fmt(digits).format(int(self.value))
            
            if(power == 0 ):
                if(float(self.LowError) == float(self.HighError)):
                    self.string='$' + self.ExpectedValue + '\\pm' +  self.LowError + '$' 

                if(float(self.LowError) != float(self.HighError)):
                    self.string='$' + self.ExpectedValue + '_{-' + self.LowError + '}^{+' + self.HighError + '}$'
            else:
            #in case of scientific notation             
                if(float(self.LowError) == float(self.HighError)):
                    self.string='$\\left(' + self.ExpectedValue + '\\pm' +  self.LowError + '\\right)\\times10^{' + str(power) + '}$' 

                if(float(self.LowError) != float(self.HighError)):
                    self.string='$\\left(' + self.ExpectedValue + '_{-' + self.LowError + '}^{+' + self.HighError + '}\\right)\\times10^{'+str(power)+'}$'
            
#        print(string)
       
###Class methods

# return LaTeX-like string with value and error
    def  get_latex_string(self):
        return self.string

#return expected value
    def get_expected_value(self):
        return self.value
#return low error
    def get_low_error(self):
        return self.mn
#return high error
    def get_high_error(self):
        return self.mx

####################################################
####################################################
####################################################
'''
This class deal with expressions where the error is symmetric, e.g.:
    ExpectedValue \pm error
'''

class value_and_symerror(value_and_error):
    def __init__(self, ExpectedValue, error):
        value_and_error.__init__(self, ExpectedValue - error, ExpectedValue, ExpectedValue + error)


