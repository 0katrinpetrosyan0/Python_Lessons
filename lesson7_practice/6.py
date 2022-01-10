# 6. Write a Python program to remove duplicates from a list.
#     lst = [10, 23, 45, 10, 89, 45, 45, 23]
#     output: [10, 23, 45, 89]

lst = [10, 23, 45, 10, 89, 45, 45, 23]
result = []
for i in lst:
    if i not in result:
        result.append(i)
print(result)

# i = 0
# while i <len(lst):
#     if lst[i] in lst[i+1:]:
#         lst.pop(i) 
#     else:
#         i += 1

# print(lst)

# print(list(set(lst)))  # not worked for output
