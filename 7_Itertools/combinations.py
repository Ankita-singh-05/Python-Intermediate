# Combinations function will make all possible combinations with a specified length
 
from itertools import combinations, combinations_with_replacement

a = [1,2,3,4]
# len arg is mandatory
comb = combinations(a, 2)
print(list(comb))
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]