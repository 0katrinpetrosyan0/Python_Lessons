# 56. Ունենք string-ներով ցուցակ, հեռացնել այն string—ները, որոնք պարունակում են միայ մեկ բառ։
# Ունենք : ['Good for you guys', 'Give me more good programs', 'Garry', 'Say yes, say no', 'Maybe']
# Արդյքունք : ['Good for you guys', 'Give me more good programs', 'Say yes, say no']

list1 =  ['Good for you guys', 'Give me more good programs', 'Garry','hey', 'Say yes, say no', 'Maybe']

i = 0
while i < len(list1):
    if " " not in list1[i]:
        list1.pop(i)
    else:
        i +=1
print(list1)
    