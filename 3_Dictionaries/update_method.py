# Update method is used to merge 2 dictionaries

my_dict = {"name": "Ankita", "age": 20, "city": "pune", "email": "sdgshd@abc.com"}
my_dict2 = dict(name="Yash", age= 9, city= "Pune")


# update will merge the both the dict in such a way that if the same key values are present in another dict then it is overwritten
my_dict.update(my_dict2)
print(my_dict)