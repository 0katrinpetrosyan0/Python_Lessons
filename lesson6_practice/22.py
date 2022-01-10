# 22. Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers
#  smaller than the specified number.

def cube(n):
    total = 0
    n -= 1
    while n > 0:
        total += n**3
        n -=1
    print(total)
cube(5)

# n = int(input())
# _sum = 0
# for num in range(n + 1):
#     _sum += num **3