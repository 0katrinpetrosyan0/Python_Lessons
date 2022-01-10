def rec(n):
    print(n)
    if n == 0:
        return 
    rec(n-1)
    print(n**2)