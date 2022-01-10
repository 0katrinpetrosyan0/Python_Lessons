# 5. Write a Python program to access a function inside a function. 
# Provide arguments to both of them and print sum of them.

def first(a):
        def second(b):
                nonlocal a
                return 4 + b
        return second

func= first(4)
print(func(4))