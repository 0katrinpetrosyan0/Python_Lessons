# list = [1, 2, 3]
# i = list.index(2)
# print(i)
list = [2, 6, 48, 56, 56, 64, 69]

def index(list, first, last, element):
    while first <= last: 
        middle = (first + last) // 2
        if element > list[middle]:
            first = middle + 1
        elif element < list[middle]:
            last = middle - 1
        else:
            return middle
    return -1

print(index(list,0,len(list)-1, 64))
