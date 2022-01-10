#2. Write a Python program to read a file line by line and store it into a dict where keys are the line numbers
# and the values are lines.

#enumerate(iterable) -> (0,it1), (1,it2) ...
#do for loop for see result
# print(enumerate(['a', 'b', 'c']))  # -> (0, a), (1, b) (2, c)

# for i , el in enumerate(['a','b']):  # we can add 2nd argument ,too like (['a','b'], 1) will start from 1
#     print(i,el)


print({n : n** 2 for n in range(5)}) # example for dict comp


file = open('ex.txt')
d = {i:l[:-1] for i,l in enumerate(file, 1)} #[:-1] - for delete /n
print(d)