#Task 1: Calculate Factorial Using a Function 

def factorial (num):
    if num == 1:
        return 1
    else:
         fact = num * factorial(num-1)
         return fact
    
num = int(input("enter your number:"))
result = (factorial(num))
print(f"the factorial of {num} is {result}")


#Task 2: Using the Math Module for Calculations

number = int(input("enter your number here :"))

import math

def squareroot(number):
    square = math.sqrt(number)
    return square

def logarithm(number):
    log = math.log(number)
    return log
def sine_value(number):
    sin = math.sin(number)
    return sin

print(f"square root :{squareroot(number)}")

print(f"logarithm:{logarithm(number)}")

print(f"sine : {sine_value(number)}")