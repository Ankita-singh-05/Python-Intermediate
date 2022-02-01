my_string = "Hello World"

# REPLACE
print(my_string.replace("World", "Universe")) # Hello Universe

# If there is typo mistake in the string then it will not replace
# It will return the original string
print(my_string.replace("Worrld", "Universe")) # Hello World