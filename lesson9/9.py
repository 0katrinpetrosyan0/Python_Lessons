#.  9. Write a function that recevies a tuple with even number of elements and prints the 
#.      first half values in one line and the last half values in another line.
def tupl(a):
    print(a[:len(a) // 2 ])
    print(a[len(a) // 2 : ])
    print(a)
a =(1,2,3,4)
tupl(a)