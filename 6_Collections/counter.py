# Counter Collection -- Counter is a container that stores the elements as dictionary keys and their counts as dictionary values.

from collections import Counter

a = "adbsjdbsbfnaaa"
my_counter = Counter(a)
print(my_counter)
# It will return all the string character as key and their count as values
# O/p - Counter({'a': 4, 'b': 3, 'd': 2, 's': 2, 'j': 1, 'f': 1, 'n': 1})

