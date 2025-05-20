# Task 1: Perform Basic Mathematical Operations
# Problem Statement: Write a Python program that does the following:
# 1.  Takes two numbers as input from the user.
# 2.  Performs the basic mathematical operations on these two numbers:
# o	Addition
# o	Subtraction
# o	Multiplication
# o	Division
# 3.  Displays the results of each operation on the screen.

print("Enter two numbers:")
num1 = float(input("Number 1: "))
num2 = float(input("Number 2: "))
print("Performing basic mathematical operations...")
# Addition
addition = num1 + num2
print(f"Addition: {addition}")
# Subtraction
subtraction = num1 - num2
print(f"Subtraction: {subtraction}")
# Multiplication
multiplication = num1 * num2
print(f"Multiplication: {multiplication}")
# Division
if num2 != 0:
    division = num1 / num2
    print(f"Division:  {division}")
else:
    print("Division: Cannot divide by zero.")