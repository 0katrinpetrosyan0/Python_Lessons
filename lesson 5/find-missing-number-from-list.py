list = [0,1,2,3, 4,5,6,8]

print([x for x in range(len(list)) if x not in list])

for i in list:
    sum1 = sum(list[:-1]) - 1
    sum1 += i
print(i)