# 2․ Գրել Python ծրագիր՝ ցուցակի ցանկացած 2 տարր տեղերով փոխելու համար։
lst = [12, 35, 9, 56, 24]

def swapList(lst):
     
    lst[1], lst[2] = lst[2], lst[1]
 
    return lst
     
print(swapList(lst))