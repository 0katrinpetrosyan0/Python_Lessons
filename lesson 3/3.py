# 3-Գրել ծրագիր, որը կստանա input և կտպի այդ էլեմենտի քանակը լիստում
#     my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
x = int(input("say an element : "))

my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]

count = my_list.count(x)

print('Count of {x} :', count)

