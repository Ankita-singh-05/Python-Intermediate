# Update method is used to merge 2 dictionaries

my_dict = {"name": "Ankita", "age": 20, "city": "pune", "email": "sdgshd@abc.com"}
my_dict2 = dict(name="Yash", age= 9, city= "Pune")


# it will merge and the which is already present in the previous dict it will update it to the new value 
my_dict.update(my_dict2)
print(my_dict)