# Random Seed Method - When we print some random numbers and we want to print the again then it will return the same value
# Random operation with seed 1 will have the same value and seed 2 will have same value
# We can reproduce our data with random seed function
# As this numbers are reproducible it is not recommeded for the security purpose
import random

random.seed(1)

print(random.random())
print(random.randint(1, 10))
# 0.13436424411240122
# 2

# Reseeding it again
random.seed(1)
print(random.random())
print(random.randint(1, 10))
# 0.13436424411240122
# 2

random.seed(2)
print(random.random())
print(random.randint(1, 10))
# 0.9560342718892494
# 1

random.seed(1)
print(random.random())
print(random.randint(1, 10))
# 0.13436424411240122
# 2

random.seed(2)
print(random.random())
print(random.randint(1, 10))
# 0.9560342718892494
# 1
