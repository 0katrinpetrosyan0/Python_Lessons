# 25. Write a Python program to compute and print sum of two given integers (more than or equal to zero). 
# If given integers or the sum have more than 80 digits, print "overflow".    

x = int(input())
y = int(input())

sum = x+y
if sum >= sum**80 and x >= x**80 or y >= y**80:
    print("overflow")
elif (x > 0 and x < x ** 80) and (y > 0 and y < y ** 80):
    print(sum)
else:
    print("enter a positive num")