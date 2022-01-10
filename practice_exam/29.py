# Ցուցակը դարձնել dictionary-ներով ցուցակ։

test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
key_list = ["name", "number"]

n = len(test_list)
res = [{key_list[0]: test_list[idx], key_list[1]: test_list[idx + 1]}
	for idx in range(0, n, 2)]
print(str(res))
