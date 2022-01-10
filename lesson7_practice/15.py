# 15. Write a Python program to get the frequency of the elements in a list. 
#     lst = [10, 20, 60, 10, 30, 50, 60, 30, 70]
#     output: 10 -> 2
#             20 -> 1
#             60 -> 2
#             30 -> 2
#             50 -> 1
#             70 -> 1

lst = [10, 20, 60, 10, 30, 50, 60, 30, 70]
# frequency = {}
# for item in lst:
#    if item in frequency:
#       frequency[item] += 1
#    else:
#       frequency[item] = 1
# print(frequency)


i = 0
while i <len(lst):
   if lst[i] not in lst[:i]:
      print(lst.count(lst[i] ), "=>" ,lst[i])
   i += 1