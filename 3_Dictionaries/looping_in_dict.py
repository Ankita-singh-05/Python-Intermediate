my_dict = {"name": "Ankita", "age": 20, "city": "pune"}

# to print the key
for key in my_dict:
    print(key)

# this will also print the keys
for key in my_dict.keys():
    print(key)

# to print the values in the dict
for value in my_dict.values():
    print(value)

# To print the key and value together
for key,value in my_dict.items():
    print(key, value)