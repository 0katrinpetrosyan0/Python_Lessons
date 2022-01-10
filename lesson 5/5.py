# 5-Write a Python that generate new list from a given list, which will contain only even numbers. 
#     nums: [1, 3, 2, 5, 4, 7, 8]
#     output: [2, 4, 8]

nums = [1, 3, 2, 5, 4, 7, 8]
print([el for el in nums if el % 2 == 0])
