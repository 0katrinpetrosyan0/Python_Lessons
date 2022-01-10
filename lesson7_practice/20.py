# 20. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
#     lst: [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
#     output: [10,11,12]

lst = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
s2 = []
for el in lst:
    for i in lst:
        s = sum(el)
    s2.append(s)
print(lst[s2.index(max(s2))])

# n = [sum(n) for n in lst]

# print(lst[n.index(max(n))])