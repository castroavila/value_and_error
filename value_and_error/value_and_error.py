#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author           : Manuel Castro Avila <manuel.castro@inpe.br>
# @file             : value_and_error.py	
# @created          : 16-Feb-2019
# @company          : National Institute for Space Research (INPE) - São José dos Campos/SP - Brazil
# 


#import functions for significant figures and formatting

from .functions.functions import *

#colors to highlight outputs coming from errors

black ="\033[1;30" 
red ="\033[1;31" 
green ="\033[1;32" 
yellow ="\033[1;33" 
blau ="\033[1;34" 
red ="\033[1;31" 

'''
A measurement is expressed as: 
LowLimit < ExpectedValue < HighLimit

'''
class value_and_error:
      
    def __init__(self,LowLimit, ExpectedValue, HighLimit):
        self.LowLimit = LowLimit
        self.ExpectedValue = ExpectedValue
        self.HighLimit = HighLimit

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
        if (0.01 <= ExpectedValue <= 100.):
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
        global string
        if(digits < 0):

            LowError = fmt(digits).format(self.mn)
            HighError = fmt(digits).format(self.mx)
            ExpectedValue = fmt(digits).format(self.value) 
    #generate proper LaTeX string
            if ( power == 0 ):

                if(float(LowError) == float(HighError)):
                    string='$' + ExpectedValue + '\\pm' +  LowError + '$' 

                if(float(LowError) != float(HighError)):
                    string='$' + ExpectedValue + '_{-' + LowError + '}^{+' + HighError + '}$'
            else:
            #in case of scientific notation             
                if(self.mn == self.mx ):
                    string='$\\left(' + ExpectedValue + '\\pm' +  LowError + '\\right)\\times10^{' + str(power) + '}$' 

                if(self.mn != self.mx):
                    string='$\\left(' + ExpectedValue + '_{-' + LowError + '}^{+' + HighError + '}\\right)\\times10^{'+str(power)+'}$'
             
        
        else:
            LowError = fmt(digits).format(round(self.mn))
            HighError = fmt(digits).format(round(self.mx))
            ExpectedValue = fmt(digits).format(round(self.value))

    #generate proper LaTeX string

    # These linies should deal with expressions like
    # 92.81 \pm 3 ==> 93 \pm 3
    # 92.81 \pm 30  ==> 90 \pm 30
    # ....
            order = int(round(self.value)/pow(10,digits))
            value = pow(10, digits)*order
            ExpectedValue = fmt(digits).format(int(value))
            
            if(power == 0 ):
                if(float(LowError) == float(HighError)):
                    string='$' + ExpectedValue + '\\pm' +  LowError + '$' 

                if(float(LowError) != float(HighError)):
                    string='$' + ExpectedValue + '_{-' + LowError + '}^{+' + HighError + '}$'
            else:
            #in case of scientific notation             
                if(float(LowError) == float(HighError)):
                    string='$\\left(' + ExpectedValue + '\\pm' +  LowError + '\\right)\\times10^{' + str(power) + '}$' 

                if(float(LowError) != float(HighError)):
                    string='$\\left(' + ExpectedValue + '_{-' + LowError + '}^{+' + HighError + '}\\right)\\times10^{'+str(power)+'}$'
            
#        print(string)
       
###Class methods

# return LaTex-like string with value and error
    def  get_latex_string(self):
        return string

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
This class deal with expressions where the error is symetric, e.g.:
    ExpectedValue \pm error
'''

class value_and_symerror(value_and_error):
    def __init__(self, ExpectedValue, error):
        value_and_error.__init__(self, ExpectedValue - error, ExpectedValue, ExpectedValue + error)


