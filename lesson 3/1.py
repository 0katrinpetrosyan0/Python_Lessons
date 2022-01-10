# 1-Գրել ծրագիր, որը կստանա input և կգտնի հետևյալ [10, 30, 4, -6] լիստում այդ էլեմենտի index-ը, չգտնելու դեպքում տպել -1

list = [10, 30, 4, -6]
x = int(input("say any element from list : "))

print(list.index((x))) if x in list else print(-1)
    