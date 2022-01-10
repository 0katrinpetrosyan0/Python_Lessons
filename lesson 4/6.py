# 6-Modify the first item (22) of a list inside a following tuple to 222
# tuple: (11, [22, 33], 44, 55)
# output: (11, [222, 33], 44, 55)

t = (11, [22, 33], 44, 55)
t[1][0] = 222
print(t)
