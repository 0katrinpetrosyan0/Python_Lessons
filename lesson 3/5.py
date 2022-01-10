#5-Գրել ծրագիր, որը կհաշվի լիստի զույգ էլեմենտների գումարը և կենտ էլեմենտների գումարը

lst = [1,2,3,4,5,6,2]

result1 = 0 
result2 = 0 
for i in lst: 
    if not i % 2: 
       result1 += i
    else:
        result2 += i
print(result1)
print(result2)
