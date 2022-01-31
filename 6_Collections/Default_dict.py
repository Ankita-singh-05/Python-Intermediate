# Default Dictionary - It is also similar to the default dict container with the only difference that it will have a default value if the key has not been set yet

from collections import defaultdict

default_dict = defaultdict(int)
default_dict["a"] = 1
default_dict["b"] = 2
print(default_dict)
# defaultdict(<class 'int'>, {'a': 1, 'b': 2})

# Accessing the key
print(default_dict["a"]) #1
print(default_dict["b"]) #2

# If the key is not present then it will return default value of an int i.e 0
print(default_dict["c"]) #0

default_dict = defaultdict(float)
# If we want default value as float then it will return 0.0
default_dict = defaultdict(list)
# If we want default value as list then it will return an empty list []