my_string = "Hello World"

# Uppercase
print(my_string.upper())

# Lowercase
print(my_string.lower())

# STARTS WITH
print(my_string.startswith("Hello")) #True
print(my_string.startswith("World")) #False

# ENDS WITH =====================
print(my_string.endswith("World")) #True
print(my_string.endswith("Hello")) #False

# FIND ======================
# to find the index of the element
print(my_string.find("o"))

# If index is not find then it will return -1
print(my_string.find("q"))

# COUNT ======================
# To count the elements in the string
# If element is not present then 0 is return
print(my_string.count("o")) #2

print(my_string.count("z")) #0
