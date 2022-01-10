# 13. Write a Python program to concatenate a list of strings to one string
#     list_of_colors = ['Red', 'White', 'Black'], output: 'Red-White-Black'

list_of_colors = ['Red', 'White', 'Black']

list = "-".join(list_of_colors)
print(list)