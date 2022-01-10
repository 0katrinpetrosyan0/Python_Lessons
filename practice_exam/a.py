list1 =  [['p', 'y', 't', 'h', 'o', 'n'], ['i', 's'], ['t', 'h', 'e'], ['b', 'e', 's', 't']]

str = ''
for i in list1:
    for j in i:
        str += j
print(str)



# s1 = {1,1,2,2,2,3,3,4,4,4,4,5}

# s2 = {1,2,4,6,6,10}

# print(len(s1 | s2))

# nums = [1,2,3,4,5]

# nums.append(nums[:])

# print(len(nums))

# lst = ['a', 'b', 'c', 'd', 'e','f']

# dct = {k: v for v, k in enumerate(lst)}

# print(dct)

# lst1= [1,2,3]
# lst2 = [4,5,6]

# lst3 = lst1.extend(lst2)

# print(lst3)

# def func(n):
#     for i in range(-1,5,2):
#         n+=i
#         n-=3
#     print(n+1)
# func(5)

# lst1 = [1,2,3,4,[0,0,0]]

# lst2 = lst1[:]

# lst1[-1][-1] = 10
# print(lst2)

# nums = [1,2,3,4,1]

# for n in nums:
#     nums[n] = 0
#     print(nums)

# a = 10
# b=20

# c = (a+b) / 5
# print(b%a + a ** c)


# elem = {'a':1, 'b': 2, 'c':3,'d':4}
# result = ''
# for i in elem:
#     result += i
# print(result)

# def inc(lst, stp):
#     i = 0
#     while i < len(lst):
#         lst[i] = lst[i] + stp
#         i+=1
# nums = [1,3,5]
# inc(nums,2)
# print(nums)

# lst = [2,3,4,5,7,10,14]
# lst2= [el for el in lst[::2] if el % 2 == 0]
# print(lst2)

# nums = [1,2,3,4,5]

# nums.append(nums[:])

# print(len(nums))


# s1 = {1,1,2,2,2,3,3,4,4,4,4,5}

# s2 = {1,2,4,6,6,10}

# print(len(s1 | s2))


# x = 10

# def f1():
#     return x

# def f2(x):
#     def f3():
#         return x
#     return f3

# f4 = f2(x)
# x = 19
# print(f1(), f4())