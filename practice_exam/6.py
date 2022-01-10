# 6․ Գրել Python ծրագիր, որը կստուգի արդյոք տրված էլեմենտը գտնվում է ցուցակում։

lst = [ 1, 6, 3, 5, 3, 4 ]
 
print("Checking if 4 exists in list ( using loop ) : ")
 
for i in lst:
    if(i == 4) :
        print (i)
## or 

if (4 in lst):
    print ("Element Exists")