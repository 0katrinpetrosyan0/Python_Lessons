#  Գրել ծրագիր, որը կհաշվի զույգ թվերի և կենտ թվերի քանակը։
list1 = [10, 21, 4, 45, 66, 93, 1]

even_count, odd_count = 0, 0
for num in list1:
	if num % 2 == 0:
		even_count += 1
	else:
		odd_count += 1
print(even_count)
print(odd_count)
