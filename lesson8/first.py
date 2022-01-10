# with open('ex.txt') as file:
#     for _, line in range(5), file:
#         print(line)

# with open('ex.txt') as spam:
#     for i in range(5):
#         print(spam.readline()[:-1])

#open and replace text from file
file = open('ex.txt')
content = file.read().replace('h', 'g')
print(content)

#open and write
file=open('ex.txt', 'w')
file.write(content)