#read first 4 lines from file.txt
line = 4
with open("file.txt") as file:
    print(file.readlines()[:line])

#if we want to remove from readlines list the end /n do this:

lines = [line[:-1] for line in file.readlines()]

# for print file lines:
for line in file:
    print(file)
