# 14. Write a Python program to test whether all numbers of a list is greater than a given number. Number get from input
#     numbers = [28, 56, 44, 32, 68, 85]

num = int(input("say a num: "))

numbers = [28, 56, 44, 32, 68, 85]

print(all(num > el for el in numbers))

