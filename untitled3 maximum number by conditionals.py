# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 10:56:37 2020

@author: Nikhil
"""

num1 = float(input("please enter the first number: "))
num2 = float(input("please enter the second number: "))
num3 = float(input("please enter the third number: "))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
   largest = num3
    
print("the largest number is : ",largest)
    
    











