# Հեռացնել դատարկ ցուցակները ցուցակից։
test_list = [5, 6, [], 3, [], [], 9]
res = [ele for ele in test_list if ele != []]

print (str(res))
