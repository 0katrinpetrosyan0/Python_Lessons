list1 = [5 , 9, 12]
list2 = [4, 8 ,15,16]
list3 = []
i = j = 0

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        list3.append(list1[i])
        i += 1
    else:
        list3.append(list2[j])
        j += 1
print(list3 + list1[i:] + list2[j:])




# list3 = []
# for i in list1:
#     for j in list2:
#         if j <= i:
#             list3.append(j)
#     list3.append(i)


# print(list3)
