# 8-Write a Python program to convert a tuple of string values to a tuple of integer values
# tuple: (('333', '33'), ('1416', '55')) output: ((333, 33), (1416, 55))

tup = (('333', '33'), ('1416', '55'))

print(tuple((int(t[0]), int(t[1])) for t in tup))