from itertools import product

a = [1,2]
b = [3,4]
prod = product(a, b)
print(prod) # <itertools.product object at 0x00000200541F93B8>

print(list(prod)) 
# [(1, 3), (1, 4), (2, 3), (2, 4)]

a = [1,2]
b = [3]
prod = product(a, b, repeat=2)
print(list(prod))
# [(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]