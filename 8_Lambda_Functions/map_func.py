# map(func, seq)

a = [1,2,3,4,5]
b = map(lambda x: x * 2, a)
print(list(b)) # [2, 4, 6, 8, 10]

# list comprehensions

c = [x*2 for x in a]
print(c) # [2, 4, 6, 8, 10]