# 19. Write a Python program to move all zero digits to end of a given list of numbers
#     lst = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
#     output: [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
arr = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]

# x=[i for i in arr if i!=0]
# y=[i for i in arr if i==0]
# x.extend(y)
# print(x)


for i in arr:
    if i == 0:
        arr.append(i)
        arr.remove(i)
print(arr)


# l = 0
# r = len(arr)-1
# while(not arr[r]):
#     r -= 1
# while(l < r):
#     if(arr[l] and arr[r]): l += 1
#     if(arr[l] and not arr[r]): r -= 1
#     if(not arr[l] and arr[r]): 
#         arr[l], arr[r] = arr[r], arr[l]
#         r -= 1
#         l += 1
#     if(not arr[l] and not arr[r]): r -= 1 

# print(arr) 
