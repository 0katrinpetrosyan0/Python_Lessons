# 16. Write a Python program to count the number of elements in a list within a specified range.
#     lst = [1, 1, 3, 2, 3, 4, 5, 3, 8, 1]
#     example: n = 3   
#              range -> (2, 8)
#              output: 3
lst = [1, 1, 3, 2, 3, 4, 5, 3, 8, 1]


# c = 0
# for i  in lst[2:8]:
#     if i == 3:
#         c += 1
# print(c)

print(lst[2:8].count(3))

