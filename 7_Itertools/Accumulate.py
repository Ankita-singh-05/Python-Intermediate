# Accumulate function makes an iterator that returns accumulated sums or binary function that will given as input
# By default it will compute the sum

from itertools import accumulate
import operator

a = [1,2,3,4]
acc = accumulate(a)
print(a) #[1, 2, 3, 4]
print(list(acc)) 
# [1, 3, 6, 10] --> 1 + 2 = 3, 3 + 3 = 6, 6 + 4 = 10

# Multiplication
a = [1,2,3,4]
acc = accumulate(a, func=operator.mul)
print(list(acc))
# [1, 2, 6, 24]
# 1*2 = 2, 2*3 = 6, 6*4 = 24

a = [1,2,8,3,6,4]
acc = accumulate(a, func=max)
print(list(acc))
# [1, 2, 8, 8, 8, 8]