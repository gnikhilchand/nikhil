# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:49:40 2020

@author: Nikhil
"""
# swapping of two numbers
x = input("please enter the value of x: ")
y = input("please enter the value of y: ")

temporary_variable = x
x = y
y = temporary_variable

print("the value of x after swapping: ",x)
print("the value of y after swapping: ",y)