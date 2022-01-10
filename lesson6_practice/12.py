# 12. Write a Python program to calculate the sum of the digits in an integer.
n = abs( int( input( "Enter number: " ) ) )
sum = 0
while n:
    sum += n % 10
    n //= 10 
print(sum)