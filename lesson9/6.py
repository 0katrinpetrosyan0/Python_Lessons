# 6. Define a function that can accept two strings as input and print the string with 
# maximum length in console. If two strings have the same length, then the function should 
# print all strings line by line.

f  = input("First  : ")
s = input("Second : ")
def str(f,s):
    if len(f) > len(s):
        print(f)
    elif len(s) > len(f):
        print(s)
    else:
        print(f)
        print(s)
str(f,s)
