# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 11:55:05 2020

@author: Nikhil
"""

year = int(input("enter the year: "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("the year is a leap year",year)
        else:
            print("the year is not a leap year",year)
    else:
        print("the year is a leap year",year)
else:
    print("the year is not a leap year",year)
    
    
    