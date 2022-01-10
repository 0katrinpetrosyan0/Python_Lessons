# 3-Write a Python program to convert a given list of integers and a tuple of integers in a list of strings and print result.
#     nums_l: [1,2,3,4]
#     nums_t: (10, 20, 30, 40)
#     ouput: 
#            List of strings:
#            ['1', '2', '3', '4']
#            Tuple of strings:
#            ('0', '1', '2', '3')

list_nums = [1, 2, 3, 4]
tuple_nums = 10, 20, 30, 40

print([str(x) for x in list_nums])
print(tuple(str(y) for y in tuple_nums))
