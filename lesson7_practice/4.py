# 4. Write a Python program to check if all items of a given list of strings is equal to a given string.
#     example: lst = ["green", "green", "green", "green"], word = "green"
#              output: True

lst = ["green", "green", "green", "green"]

print(all(word == "green" for word in lst))

# word = "green"
# print(word == list(set(lst))[0] and len(set(lst)) == 1)