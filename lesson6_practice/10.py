# 10. Write a Python program to sum of three integers. However, if two values are equal sum will be zero. Integers get from input

a = int(input())
b = int(input())
c = int(input())

print(0 if a == b or b == c or c == a else a + b + c)
