my_dict = {"name": "Ankita", "age": 20, "city": "pune"}


# ways to find that element is present in the dic or not
if "lastname" in my_dict:
    print(my_dict["lastname"])
else:
    print("not in dictionary")


# Try and Except
# if try block doesn't satisfy the condition then exception is thrown
try:
    print(my_dict["name"])
except:
    print("Error")


