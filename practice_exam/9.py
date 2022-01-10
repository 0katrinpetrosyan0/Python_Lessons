# 9․ Նշել մի քանի եղանակ ցուցակը կլոնավորելու համար։
lst1 = [4, 8, 2, 10, 15, 18]


def Cloning(li1):
    li_copy = [i for i in li1]
    return li_copy
  
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)


##or

def Cloning(lst1):
    li_copy = list(lst1)
    return li_copy
  
lst2 = Cloning(lst1)
print(lst1)
print(lst2)

##or

def Cloning(li1):
    li_copy =[]
    for item in li1: li_copy.append(item)
    return li_copy
  
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
