# 10. Write a Python program to get the difference between the two lists.
#     lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     lst2 = [1, 3, 4, 5, 7, 9]
#     output: [2, 6, 8]

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst2 = [1, 3, 4, 5, 7, 9]

print([i for i in lst1 + lst2 if i not in lst1 or i not in lst2])

