# 10-Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples
# list: [(1, 2), (2, 3), (3, 4)] ouptut: [3, 5, 7]
arr = [(1, 2), (2, 3), (3, 4)]
res=[]

for x,y in arr :
	res.append(x + y)
print(res)