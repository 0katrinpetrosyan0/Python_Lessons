
# 11. Write a Python program to convert a list of characters into a string.
#     lst = ['P', 'y', 't', 'h', 'o', 'n']
#     output: 'Python'

lst = ['P', 'y', 't', 'h', 'o', 'n']
new = ""
for char in lst:
    new += char 
print(new)

# print(new.join(lst))
