# Permutations - permutation will return all possible orderings of an input

from itertools import permutations

a = [1,2,3]
perm = permutations(a)
print(list(perm))
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# We can also specify the length of an argument as an 2nd argument
perm = permutations(a, 2)
print(list(perm)) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]