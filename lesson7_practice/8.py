# 8. Write a Python program that takes two lists and returns True if they have at least one common member.
#     lst1 = [10, 20, 30, 40, 50, 11]
#     lst2 = [1, 2, 11, 3, 4, 5]
#     output: True

lst1 = [10, 20, 30, 40, 50, 11]
lst2 = [1, 2, 11, 3, 4, 5]

# bool = False
# for x in lst1:
#     for y in lst2:
#         if y == x:
#             bool = True
# print(bool)

#
print(bool(set(lst1) & set(lst2)))

# flag = True

# for el in lst1:
#     if el in lst2:
#         flag = True
#         break

# print(flag)
