# 15. Write a Python program to count the number of occurrence of a specific character in a string. Character get from input
#     string: "The quick brown fox jumps over the lazy dog."  
#     input: 'o', output: "Number of occurrence of 'o' in the said string: 4

str = "The quick brown fox jumps over the lazy dog." 

char = input("enter a letter: ")

count = 0
for x in str:
    if x == char:
        count += 1
print(count)