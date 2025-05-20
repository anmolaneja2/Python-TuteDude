# Task 1: Calculate Factorial Using a Function 


# Problem Statement: Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output


def factorial(n):
    if n==0 or n==1:    
        return 1
    else:
        result=factorial(n-1)*n
        return result
    
# Example usage
number = int(input("Enter a number: "))
result = factorial(number)
print(f"The factorial of {number} is: {result}")