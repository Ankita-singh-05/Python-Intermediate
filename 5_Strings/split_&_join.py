my_string = "How are you doing"

# In split method default argument or delimiter is space i.e split(" ")
my_list = my_string.split()

print(my_list) #["How", "are", "you", "doing"]


my_string = "How,are,you,doing"
my_list = my_string.split() #['How,are,you,doing']
# default delimiter is space and in the above string there is no space so it will be consider as 1 element in the list
print(my_list)

my_string = "How,are,you,doing"
my_list = my_string.split(",")
print(my_list) #['How', 'are', 'you', 'doing']


# If we want to convert the list again to string then we use join
new_string = "".join(my_list)
print(new_string) #Howareyoudoing

new_string = " ".join(my_list)
print(new_string) #How are you doing