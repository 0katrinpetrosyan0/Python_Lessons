# 17. Write a Python program to find common items from two lists.
#     lst1 = [10, 20, 30, 40, 50, 11]
#     lst2 = [1, 2, 11, 3, 4, 5]
#     output: [11]

lst1 = [10, 20, 30, 40, 50, 11]
lst2 = [1, 2, 11, 3, 4, 5]
# print( list ( set(lst1) & set(lst2) ) )

print([el for el in lst1 if el in lst2 ])