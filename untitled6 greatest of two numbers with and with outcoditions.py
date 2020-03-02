# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:20:11 2020

@author: Nikhil
"""
# with conditions
num1 = float(input("please enter first number: "))
num2 = float(input("please enter second number: "))

if (num1 > num2):
    print("num1 is greater: ",num1)
elif (num2 > num1):
    print("num2 is greater: ",num2)
else:
    print("both are equal ")
    
#with out conditions
list1 = [5,8]
max(list1)
    