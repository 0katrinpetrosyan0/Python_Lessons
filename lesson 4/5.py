#5-Check if all items in the following tuple are the same
# tuple: (45, 45, 45, 45)
# ouput: True
a = 45, 45, 45, 45

print(all(el == 45 for el in a))