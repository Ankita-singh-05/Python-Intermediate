# Random Module - This is used to genrate the pseudo random numbers for various distribution.
# It is called as pseudo random because the numbers seem random, but they are reproducible.
import random

# random.random() - this funct is used to print a random float in the range from zero to one
a = random.random()
print(a)
# 0.44938311930650754

# It will print the random float in the range 1 to 10
a = random.uniform(1, 10)
print(a)
# 9.084106487390342

# It will print the random numbers between the given integer and it will also include the upper bound i.e 10
a = random.randint(1, 10)
print(a)

# It will print the random numbers between the given integer but it not include the upper bound i.e 10
a = random.randrange(1, 10)
print(a)

# 3.01.50
