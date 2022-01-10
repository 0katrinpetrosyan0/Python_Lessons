#.  10. Write a function called matches that takes two strings as 
#.       arguments and returns how many matches there are between the strings. 
#.       match is where the two strings have the same character at the same index. 
#.       For instance, 'python' and 'path' match in the first, third, and fourth 
#.       characters, so the function should return 3.
a = input("type your first string: ")
b = input("type your second string: ")
def matches(a,b):
    if len(a) < len(b):
        b,a = a,b
    count = 0 
    for i in range(len(b)):
        if a[i] == b[i]:
            count+=1
    print(count)
    print(a,b)
matches(a,b) 