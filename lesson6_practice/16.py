# 16. Write a Python program to check if a number is positive, negative or zero. Get number from input

x = int(input("Enter a number: "))

if x > 0:
    print("x is +")
elif x < 0:
    print("x is -")
else:
    print(0)