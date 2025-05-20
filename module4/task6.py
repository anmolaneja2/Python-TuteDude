
# Task 2: Using the Math Module for Calculations
 
# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)
# 3.   Displays the calculated results.
import math

number=float(input("Enter a number: "))

sqroot=math.sqrt(number)
log=math.log(number)
sine=math.sin(number)
print(f"Square Root: {sqroot}")
print(f"Logarithm: {log}")  
print(f"Sine: {sine}")  