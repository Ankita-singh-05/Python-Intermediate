my_string = "     Hello World    "

# This will not remove the space because strings are immutable
# So we need to assign the original string to new string
# my_string.strip()

my_string = my_string.strip()
print(my_string)