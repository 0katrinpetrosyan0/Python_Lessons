# 7-Write a Python program to calculate the average value of the numbers in a given tuple of tuples
# tuple: ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)) output: [30.5, 34.25, 27.0, 23.25]

t = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)) 
tmp = 0
avg = []

for i in range(len(t)) :
    for j in range(len(t)):
        tmp += t[j][i]
    avg.append(tmp / len(t[i]))
    tmp = 0
print(avg)