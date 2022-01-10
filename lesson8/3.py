# 3. Write a Python program to combine each line from first file with the corresponding line in second file in a dict where 
# keys are the line numbers, and values are the combined lines and print the longest value of that dict.

##EXAMPLES for ZIP ================================================================================
# zip(iter1, iter2, ... iterN) -> (iter1[0], iter2[0] ... iterN[0])
#                                 (iter1[1], iter2[1] ... iterN[1])

# for t in zip([1,2,3], ['a', 'b', 'c']):
#     print(t)


# for t in zip([1,2,3], 'xy', (4,5,6)):
#     print(t)

#  ================================================================================


# with open('1.txt') as f1, open('2.txt') as f2:
#     i = 1
#     d = {}
#     s1 = f1.readline()[:-1]
#     s2 = f2.readline()
#     while s1 or s2:
#         d[i] = s1 + s2
#         s1 = f1.readline()[:-1]
#         s2 = f2.readline()
#         i += 1

def file_lyrics(lyrics):
    my_dict={}
    for i in lyrics:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    return my_dict

var = open("ex.txt")
print(file_lyrics(var.read().split()))




#
# _max = ''
# for v in d.values():
#     if(len(v) > len(_max)):
#         _max = v


