# 13. Write a Python program to find the second smallest number in a list. 
#     lst = [10, 10, 20, 30, 40, 50, 60]
#     output: 20
lst = [10, 10, 20, 30, 40, 50, 60]

print(sorted(set(lst))[1]) 

# _min = min(lst)
# while _min in lst:
#     lst.remove(_min)
# print(min(lst))

lst1 = list(set(lst))
lst1.remove(min(lst1))
print(min(lst1))