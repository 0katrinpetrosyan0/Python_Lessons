# 21. Write a Python function to find the maximum and minimum numbers from a sequence of numbers.

list = [3,4,9]

min = list[0]
max = list[0]

for i in list:
    if i > max:
        max = i
    elif i < min:
        min = i
print(min, max)