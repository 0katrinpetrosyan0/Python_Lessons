# 17. Write a Python program, that get from input number and to remove the item by number index from a specified list.
    
lst = [15, 28, 25, 20, 30, 48, 56, 109, 157]
num = int(input())

for i in range(len(lst)):
    if i == num:
        lst.remove(lst[i])
print(lst)