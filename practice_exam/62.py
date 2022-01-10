# list-i amboxj tvery vor > en tvats min-ic u < tvac max-ic

seq = input().split(',')
_min = int(input())
_max = int(input())
print([int(el) for el in seq if ',' not in el and _min < int(el) < _max])

