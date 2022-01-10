# vory kstana tveri hajordakanutyun ajd tveri mediany, ete elementi qanaky zuyga klni mejtexi 2 i +-i kesy

seq = input().split(',')
seq = [float(el) for el in seq]

length = len(seq)
print(seq[length//2] if length % 2 !=0 else (seq[length//2-1] + seq[length // 2])/2)