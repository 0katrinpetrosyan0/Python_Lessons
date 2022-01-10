# Ստանալ նոր ցուցակ ցուցակներով, որը կպարունակի 2 ցուցակների ոչ ընդհանուր անդամ ցուցակները։
# Ունենք ցուցակ 1 : [[4, 5], [100, 500], [11, 77]]
# Ունենք ցուցակ 2 : [[11, 77], [2, 3], [100, 500]]
# Արդյունք : [[4, 5], [2, 3]]

test_list1 = [ [1, 2], [3, 4], [5, 6] ]
test_list2 = [ [3, 4], [5, 7], [1, 2] ]

res_list = []
for i in test_list1:
	if i not in test_list2:
		res_list.append(i)
for i in test_list2:
	if i not in test_list1:
		res_list.append(i)
print (str(res_list))
