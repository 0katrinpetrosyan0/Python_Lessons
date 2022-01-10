#2. Write a Python function to calculate the factorial of a 
# number (a non-negative integer). The function accepts the 
# number as an argument. 

n = int(input("Input a number : "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(n))