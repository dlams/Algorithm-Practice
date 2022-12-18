from itertools import permutations, combinations, combinations_with_replacement, product

_list = [1, 2, 3, 4]

print(  list(combinations(_list, 2))  )
print(  list(permutations(_list, 2))  )
print(  list(combinations_with_replacement(_list, 2))  )
print(  list(product(_list, repeat = 2))  )
