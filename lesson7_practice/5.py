# 5. Write a Python program to insert a given string at the beginning of all items in a list.
#     lst : [1,2,3,4], word : emp
#     ouptut: ['emp1', 'emp2', 'emp3', 'emp4']

lst = [1, 2, 3, 4]

print(['emp{0}'.format(i) for i in lst])

# print(["emp" + str(el) for el in lst])