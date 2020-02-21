# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 13:13:35 2020

@author: Nikhil
"""

# P,T,R calculation
princ_amount = float(input(" Please Enter the Principal Amount : "))
rate_of_int = float(input(" Please Enter the Rate Of Interest   : "))
time_period = float(input(" Please Enter Time period in Years   : "))
simple_interest=(princ_amount * rate_of_int * time_period) / 100
print("\nSimple Interest for Principal Amount {0}={1}".format(princ_amount,simple_interest))
  
# compound interest
import math
princ_amount = float(input(" Please Enter the Principal Amount : "))
rate_of_int = float(input(" Please Enter the Rate Of Interest   : "))
time_period = float(input(" Please Enter Time period in Years   : "))
ci_future = princ_amount*(math.pow((1+rate_of_int/100),time_period)) 
compound_int = ci_future - princ_amount
print("Future Compound Interest for Principal Amount {0}={1}".format(princ_amount,ci_future))
print("Compound Interest for Principal Amount {0} = {1}".format(princ_amount, compound_int))



