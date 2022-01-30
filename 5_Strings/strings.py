# Strings - ordered, immutable, text representation
# It is created using single or double quote

my_string = "Hello World"
print(my_string)

my_string = 'I\'m a programmer'
# \' will print ' it is escape character
print(my_string)

# Triple quotes are also used to create the string mostly used for documentation
# It is use when String goes over multiple lines
my_string = """Hello
World"""
print(my_string)

# Accessing the string
print(my_string[0])
print(my_string[-1])

# Slicing
print(my_string[1:5])

# Step index
print(my_string[::2])

