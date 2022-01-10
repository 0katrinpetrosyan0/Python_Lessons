# 9. Write a Python program to print the numbers of a specified list after removing even numbers from it.
#     lst = [1, 4, 3, 6, 5, 10, 8]
#     output: [1, 3, 5]

lst = [1, 4, 3, 6, 5, 10, 8]

print([x for x in lst if x % 2 != 0])


for i in lst:
    if i % 2 == 0:
        print(list(i))