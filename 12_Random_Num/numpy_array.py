import numpy as np

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)

# This will only shuffle the elements along the first axis
# It will never switch elements in the first axis.
np.random.shuffle(arr)
print(arr)


# NOTE - Numpy random generator uses a different number generator than the one from the python standard library.
# It also has a different seat functions
# We should use numpy seed method instead of the seed method from random module


# Both will print the same random numebers
np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(1)
print(np.random.rand(3,3))