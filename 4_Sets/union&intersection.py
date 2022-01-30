odds = set([1,3,5,7,9])
evens = {0,2,4,6,8,10}
prime = set([2, 3, 5, 7])

# Calculating the unions

u = odds.union(evens)
# u = odds.union(evens,prime)
print(u)

i = odds.intersection(prime)
print(i) 
# {3,5,7}

i = odds.intersection(evens)
print(i)
# set()

i = evens.intersection(prime)
print(i)
# {2}