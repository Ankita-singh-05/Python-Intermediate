my_dict = {"name": "Ankita", "age": 20, "city": "pune"}

# we can use del method or pop method for deleting the key and value
del my_dict["age"]
print(my_dict)

my_dict.pop("city")
print(my_dict)

# popitem is used to delete the lastly inserted value
my_dict.popitem()
print(my_dict)