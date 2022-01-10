#11. In this exercise you will write a function that determines whether or not a password
#.    is good. We will define a good password to be a one that is at least 8 characters long
#.   and contains at least one uppercase letter, at least one lowercase letter, and at least
#.   one number. Your function should return True if the password passed to it as its
#.   only parameter is good. Otherwise it should return False. Include a main program
#.  that reads a password from the user and reports whether or not it is good. 
print("your password should contain at least 8 characters,at least one uppercase letter, at least one lowercase letter, and at least one number")
a = input("enter your password: ")
def pas(a):
    Uppercase = False
    Lowercase = False
    numb = False
    if len(a) >= 8:
        for i in a:
            if i.isupper():
                Uppercase = True
            if i.islower():
                Lowercase = True
            if i.isdigit():
                numb = True
        if Uppercase and Lowercase and numb:
            print(True)
        else:
            print(False)
    else:
        print(False)
pas(a)