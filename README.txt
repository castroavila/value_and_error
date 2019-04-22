README.txt

:Author:	Manuel Castro Avila
:Email:		manuel.castro@inpe.br
:Date:		20-Mar-2019
		National Institute for Space Research (INPE)- São José dos Campos/SP - Brazil

####################################################################################
####################################################################################
  This script has been developed under financial support from FAPESP (Fundação  #
  de Amparo à Pesquisa do Estado de São Paulo, Brazil) under grant #2015/25972-0#
####################################################################################
####################################################################################



##Installation 
#In default python location
#Use --user option to install locally 
python3 setup.py install --user 

#Specific location 
python3 setup.py install  --prefix=/path/to/location
#Make sure to add /path/to/location into PYTHONPATH variable


#importing classes

There are two classes:
1) value_and_error --> This class handles expressions given as: LowLimit <
ExpectedValue < HighLimit
	This class is imported as: from value_and_error.value_and_error import value_and_error

2)value_and_symerror --> This class handles expressions with symmetric error,  given as: 
	ExpectedValue \pm error

The class  value_and_error has a method that allows to retrieve  the LaTeX-like
string: get_latex_string(). Same case in value_and_symerror

#Bibliography 
This script follows the theory giving in:
An introduction to error analysis: The study of uncertainties in physical
measurements, 2nd edition, John R.  Taylor, chapter 2, 1997.



