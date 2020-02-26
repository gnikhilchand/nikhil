# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 14:48:32 2020

@author: Nikhil
"""

# compound interest
import math
principal_amount = float(input(" Please Enter the Principal Amount : "))
rate_of_interest = float(input(" Please Enter the Rate Of Interest : "))
time_period = float(input(" Please Enter Time period in Years : "))
compound_interest_future = principal_amount*(math.pow((1+rate_of_interest/100),time_period)) 
compound_interest = compound_interest_future - principal_amount
print("Future Compound Interest for Principal Amount: ",principal_amount)
print("Compound Interest for Principal Amount: ",compound_interest)




