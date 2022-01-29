my_dict = {"name": "Ankita", "age": 20, "city": "pune"}

my_dictcpy = my_dict
print(my_dictcpy)

# changes made in copied dict will reflect to the original dict also
my_dict["email"] = "ansjdh@jhdjs.com"
print(my_dict)
print(my_dictcpy)

# if we want to make an actual copy of the dict then we can use copy function


my_dictcpy = my_dict.copy()
print(my_dictcpy)

# or we can use dict function
my_dictcpy = dict(my_dict)
print(my_dictcpy)