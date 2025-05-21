# Task 1: Perform Basic Mathematical Operations
# Problem Statement: Write a Python program that does the following:
# 1.  Takes two numbers as input from the user.
# 2.  Performs the basic mathematical operations on these two numbers:
# o	Addition
# o	Subtraction
# o	Multiplication
# o	Division
# 3.  Displays the results of each operation on the screen.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter The second number: "))


addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
if num2 != 0:
    division = num1 / num2
    print(f"Division:  {division}")
else:
    print("Cannot divide by zero")