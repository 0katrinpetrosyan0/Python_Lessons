# 12. Write a Python program to append a list to the second list.
#     lst1 = [1, 2, 3, 4]
#     lst2 = [7, 8, 9]
#     output: lst2 -> [7, 8, 9, 1, 2, 3, 4]

lst1 = [1, 2, 3, 4]
lst2 = [7, 8, 9]

print(lst2 + lst1)

# lst2.extend(lst1)
# print(lst2)