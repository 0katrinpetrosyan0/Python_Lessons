# 5. Write a Python program to get the difference between a input number and 17, if the number is greater than 17 return double the absolute difference.
#     example. input: 20, output: 3 
#              input: 15, output: 4

n = int(input("Enter a number: "))

print(n - 17 if n > 17 else (n - 17) **2)
