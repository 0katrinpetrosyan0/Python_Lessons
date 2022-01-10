# 4-Write a Python program to convert a given list of strings into list of lists
#     colors: ['Red', 'Green', 'Black', 'Orange']
#     output: [['R', 'e', 'd'], ['G', 'r', 'e', 'e', 'n'], ['B', 'l', 'a', 'c', 'k'], ['O', 'r', 'a', 'n', 'g', 'e']]

x = ['Red', 'Green', 'Black', 'Orange']
print([list(word) for word in x])