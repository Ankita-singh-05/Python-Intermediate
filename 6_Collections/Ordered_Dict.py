# Ordered Dictionary - It is just like regular dictionary, but they remeber the order that the items were inserted
# It remember the ordered and print the elements in sequence
# But in Python 3.7 normal dictionary also print the elements in sequence
# So it is for older versions of python

from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['a'] = 2
ordered_dict['b'] = 3
ordered_dict['c'] = 4
ordered_dict['d'] = 5
ordered_dict['e'] = 6

print(ordered_dict)
# OrderedDict([('a', 2), ('b', 3), ('c', 4), ('d', 5), ('e', 6)])

# Python 3.7 normal dict print the same result
ordered_dict = dict()
ordered_dict['a'] = 2
ordered_dict['b'] = 3
ordered_dict['c'] = 4
ordered_dict['d'] = 5
ordered_dict['e'] = 6
print(ordered_dict)
# {'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6}