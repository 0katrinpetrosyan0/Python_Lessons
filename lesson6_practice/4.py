# 4. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
#     example. n: 5, output: 615 ( 5 + 55 + 555 )

n1 = int(input())
n2 = n1 * 10 + n1
n3 = n1 * 100 + n2

print(n1 + n2 + n3)