# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:56:28 2020

@author: Nikhil
"""
#int
print(10)
print(-20)

#float
x=1.0
print(x)
print(-2.0)

#complex
x=complex(0,2)
y=complex(2,1)
print(x)
print(y)

#bool
print(True)
x=False
print(x)

#string
x=("nikhil chand")
print(x)
x=('nikhil chand')
print(x)

#index
x=[1,2,3,4,5,6]
print(x[0])
print(x[4])
print(x[0:3])
print(x[3:-1])

#sum of two numbers
x=5
y=10
print(x+y)

#arthematic operations
x=10
y=15
print(x-y)
print(x*y)
print(x/y)


#perimeter of rectangle
length=int(input("length: "))
width=int(input("width: "))
area=2*(length*width)
print("perimeter_of_rectangle:",perimeter)


#area of rectangle
length=int(input("length: "))
width=int(input("width: "))
area=length*width
print("area_of_rectangle:",area)


#area of circle
radius=int(input("radius"))
area=3.14*radius*radius
print("area_of circle:",area)

#circumference of circle
radius=int(input("radius"))
circumference=2*3.14*radius
print("circumference_of_circle:",circumference)

#diameter of circle
radius=int(input("radius"))
diameter=2*radius
print("diameter_of_circle:",diameter)


#converting cm into meter and km
cm=1000;
meter = cm / 100.0; 
kilometer = cm / 100000.0; 
print("Length in meter = " , 
               meter , "m"); 
print("Length in Kilometer = ",  
             kilometer , "km"); 
  
  #convert celcius in to farenheit 
celcius=int(input("temperature in celcius"))     
farenheit=(celcius*1.8)+32
print("tempetature_in_farenheit:",farenheit)


DAYS_IN_WEEK = 7
def find( number_of_days ):  
year = int(number_of_days / 365) 
week = int((number_of_days / 365) / DAYS_IN_WEEK) 
days = (number_of_days / 365) / DAYS_IN_WEEK   
print("years = ",year, "\nweeks = ",week, "\ndays = ",days) 
number_of_days = 200
find(number_of_days) 

#power of a number
number = int(input(" Please Enter any Positive Integer : "))
exponent = int(input(" Please Enter Exponent Value : "))
power = 1
for i in range(1, exponent + 1):
  power = power * number   
print("The Result of {0} Power {1}={2}".format(number,exponent,power))

# square root of a number
import math
number = float(input(" Please Enter any numeric Value : "))
squareRoot = math.sqrt(number)
print("The Square Root of a Given Number {0}={1}".format(number,squareRoot))

# angles of triangle
a = float(input('Please Enter the First Angle of a Triangle: '))
b = float(input('Please Enter the Second Angle of a Triangle: ')
c = 180 - (a + b)
print("Third Angle of a Triangle = ", c)

# area of a triangle with base and height
base = float(input('Please Enter the Base of a Triangle: '))
height = float(input('Please Enter the Height of a Triangle: '))
area = (base * height) / 2
print("The Area of a Triangle using",base,"and",height,"=",area)

# area of equilateral triangle
side = float(input('Enter Length of the Triangle: '))
Area = (math.sqrt(3)/ 4)*(side * side)
print("\n Area of Equilateral Triangle = %.2f" %Area)

# students subjects and marks
english = float(input("Please enter English Marks: "))
math = float(input("Please enter Math score: "))
computers = float(input("Please enter Computer Marks: "))
physics = float(input("Please enter Physics Marks: "))
chemistry = float(input("Please enter Chemistry Marks: "))
total = english + math + computers + physics + chemistry
average = total / 5
percentage = (total / 500) * 100
print("\nTotal Marks = %.2f"  %total)
print("Average Marks = %.2f"  %average)
print("Marks Percentage = %.2f"  %percentage)


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



