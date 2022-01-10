# 9-Write a Python program to check if a specified element presents in a tuple of tuples
# input: 'White' (Just for example, input must be given from user)
# tuple: (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
# output: True

tupl = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
color = str(input("Write any color : "))

x = False

for colors in tupl:
    for i in colors:
        if color == i:
            x = True
            break
print(x)
