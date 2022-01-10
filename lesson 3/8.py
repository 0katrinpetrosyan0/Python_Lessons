#8-Գրել ծրագիրր, որը կհաշվի լիստում առկա այն էլեմենտների քանակը, որոնց երկարությունը 2-ից մեծ է և առաջին ու վերջին սիմվոլները նույնն են
    # input: ['abc', 'xyz', 'aba', '1221', 'bb', 'mom'], output: 3

def count_elem_num(lst):
    c = 0
    for i in lst:
        if len(i) > 2 and i[0] == i[-1]:
            c += 1
    return c

lst = ['abc', 'xyz', 'aba', '1221', 'bb', 'mom']
for i in lst:
    z = count_elem_num(lst)

print(z)
