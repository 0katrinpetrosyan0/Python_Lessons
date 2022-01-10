# 4-Copy element 44 and 55 from the following tuple into a two variables (use only tuple unpacking)
# tuple: (11, 22, 33, 44, 55, 66)
a = 11, 22, 33,44,55,66
*rest, b,c,_ = a
print(b,c)
