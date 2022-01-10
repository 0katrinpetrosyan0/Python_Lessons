# 23. Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.
list = [1, 2 , 3, 5, 6, 7 , 8 , 9]
'''
for i in list:
    removed_element = list.pop(list[::3])
print('Removed Element:', removed_element)
'''
def remove(list):
    pos = 3-1 
    idx = 0
    l = len(list)
    while(l):
        idx = (pos + idx) % l
        print(list.pop(idx))
        l -= 1

remove(list)