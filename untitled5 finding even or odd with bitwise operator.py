# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 11:46:27 2020

@author: Nikhil
"""

#finding even or odd with bitwise operator

number = int(input("please enter the number: "))

if number&1:
    print("the number is an even number")
else:
    print("the number is an odd number")