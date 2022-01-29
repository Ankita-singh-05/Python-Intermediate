
import sys
import timeit

from numpy import number

my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes") #104 Bytes
print(sys.getsizeof(my_tuple), "bytes") #88 Bytes

print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000)) #0.0662929
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000)) #0.0104307


# Time taken to create the List is more than Tuple
# Tuple is efficient as compared to List
# For same items in the list and tuple, list takes more memory storage than tuple
# Therefore working with tuple is more efficient than list

