# Counter Collection -- Counter is a container that stores the elements as dictionary keys and their counts as dictionary values.

from collections import Counter

a = "adbsjdbsbfnaaa"
my_counter = Counter(a)
print(my_counter)
# It will return all the string character as key and their count as values
# O/p - Counter({'a': 4, 'b': 3, 'd': 2, 's': 2, 'j': 1, 'f': 1, 'n': 1})

print(my_counter.items())
# Dictionary items - dict_items([('a', 4), ('d', 2), ('b', 3), ('s', 2), ('j', 1), ('f', 1), ('n', 1)])

print(my_counter.values())
# dict_values([4, 2, 3, 2, 1, 1, 1])

print(my_counter.keys())
# dict_keys(['a', 'd', 'b', 's', 'j', 'f', 'n'])


# To get the most common element
print(my_counter.most_common(1))
# [('a', 4)]
print(my_counter.most_common(2))
# [('a', 4), ('b', 3)]

# If we add index value then it will return tuple
print(my_counter.most_common(1)[0])
# ('a', 4)

print(my_counter.most_common(1)[0][0])
# a

print(my_counter.elements())
# <itertools.chain object at 0x00000243BC564A48>

b = "aaabbbcc"
my_counter = Counter(b)
print(list(my_counter.elements()))
# ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c']

b = "bbbacbacbacba"
my_counter = Counter(b)
print(list(my_counter.elements()))
# ['b', 'b', 'b', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'c', 'c', 'c']