# 58․ Ունենք ցուցակ բաղկացած string-նախադասություններից, dictionary-ի օգնությամբ տպել ամեն բառը ինչքան
# հաճախ է կրկնվել ընդհանուր ցոցակի մեջ արտահայտված տոկոսներով։
# Ունենք ։ [“Python is best for programmers”, “All love Python”]
# Արդյունք ։  {‘Python’: 0.25, ‘is’: 0.125, ‘best’: 0.125, ‘for’: 0.125, ‘programmers’: 0.125, ‘All’: 0.125, ‘love’: 0.125}

list1 = ["Python is best for programmers", "All love Python"]

count = 0
dict1 = {}

for i in list1:
    str = i.split(" ")
    count = len(str)
    print(count)
    for word in i:
        dict1.update({word: count})
print(dict1)