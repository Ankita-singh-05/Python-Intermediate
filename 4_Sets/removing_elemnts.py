my_set = {1,2,3,4,5,4,5,2}
print(my_set)

# to remove the elements inside the set
my_set.remove(4)
print(my_set)

# Discard method is also used to remove the elements
my_set.discard(3)
print(my_set)


# difference between remove and discard is that if the element is not 
# present in the set then remove will give error on the other hand discard will print the set

