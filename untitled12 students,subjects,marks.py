# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 14:38:58 2020

@author: Nikhil
"""

# students subjects and marks
english = float(input("Please enter English Marks: "))
math = float(input("Please enter Math score: "))
computers = float(input("Please enter Computer Marks: "))
physics = float(input("Please enter Physics Marks: "))
chemistry = float(input("Please enter Chemistry Marks: "))
total = english + math + computers + physics + chemistry
average = total / 5
percentage = (total / 500) * 100
print("Total Marks: = "  ,total)
print("Average Marks: = "  ,average)
print("Marks Percentage: = "  ,percentage)
