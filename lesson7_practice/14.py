# 14. Write a Python program to get unique values from a list.
#     lst = [10, 20, 60, 10, 30, 50, 60, 30, 70]
#     output: [20, 50, 70]

lst = [10, 20, 60, 10, 30, 50, 60, 30, 70]
# for i in lst:
#     if lst.count(i) == 1: print(i)

print([el for el in lst if lst.count(el)==1])

