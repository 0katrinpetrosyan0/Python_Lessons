#. 8. Define a function which can generate a list where the values are square of numbers 
#. between n and m (both included) which are provided by user. Then the function needs to 
#. print the last 5 elements in the list.
def gen_list():
    n = int(input("First :  "))
    m = int(input("Second :  "))
    lst =[]
    for i in range(n, m+1):
        lst.append(i**2)
    print(lst[-5:])
gen_list()