# Frozen set -- It is also a collection data type, but it is a immutable form of set

a = frozenset([1,2,3,4,5,6])

# a.add(2) -- it is immutable so it will throw an error
print(a)

# Remove method also don't work with frozenset
# Union, intersection and difference works with frozenset
