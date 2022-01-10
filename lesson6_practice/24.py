# Write a Python program to reverse the digits of a given number and add it to the original

num = 123
num1 = num
revsnum = 0  

while num1 > 0:  
    remainder = num1 % 10  
    revsnum = (revsnum * 10) + remainder  
    num1 = num1 // 10  

print(num + revsnum)

#

# _sum = num + int(str(num)[::-1])
# print(int(_sum))