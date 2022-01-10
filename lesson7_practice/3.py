# 3. Write a Python program to insert an element before each element of a list.
#     lst = [10, 20, 30, 40, 50, 60, 70]
#     el = 111
#     output: [111, 10, 111, 20, 111, 30, 111, 40, 111, 50, 111, 60, 111, 70] 

lst = [10, 20, 30, 40, 50, 60, 70]

print([res for i in lst for res in (111, i)])

# for i in range(0,len(lst)*2, 2):
#     lst.insert(i,111)
# print(lst)