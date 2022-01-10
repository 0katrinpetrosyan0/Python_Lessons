# 20. Write a Python function to check whether a number is divisible by another number.
# Accept two integers values form the user.


def check():
    num1 = int(input("say a num 1: "))
    num2 = int(input("say a num 2: "))
    if not num2: 
        return False

    return not(bool(num1 % num2))
    
print(check())