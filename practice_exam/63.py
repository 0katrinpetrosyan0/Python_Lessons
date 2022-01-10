#cragir vor tpum e list-i elementy u ayd elementy qani angam e handipum

lst = [1,2,3,4,4,2]

for el in set(lst):
    print(f'{el} -> {lst.count(el)}')
