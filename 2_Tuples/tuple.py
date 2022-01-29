# Tuple - Tuple is ordered, immutable and it allows duplicate elements

myTuple = ("Ankita", "Singh", 34)
print(myTuple)

# If we want to print single element in tuple then we need to add comma at the end otherwise it will be treated as a string
myTuple = ("Ankita")
print(type(myTuple)) # it will treated as str

myTuple = ("Ankita",)
print(type(myTuple)) # it will treated as tuple


# Another way to create tuples
myTuple = tuple([23, "Ankita", "Singh"])
print(myTuple)