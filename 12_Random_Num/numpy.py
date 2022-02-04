import numpy as np

# It will produce the 1D array with three elements in it
a = np.random.rand(3)
print(a)

# this will print the 3 by 3 array 
a = np.random.rand(3, 3)
print(a)


# 0 to 10 is a range, 10 is excluded , then 3 is size
# it will print random integers  with 3 elements in it
a = np.random.randint(0, 10, 3)
print(a)
# [0 8 8]

# For higher number of size we need to define it in tuple
# this will print 3 by 4 array
a = np.random.randint(0, 10, (3,4))
print(a)
# [2 3 4 5]
# [4 6 8 1]
# [0 4 5 2]

