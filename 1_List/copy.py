list_original = ["banana", "apple", "mango"]

list_copy = list_original
list_copy.append("Orange")

print(list_copy)
print(list_original)

# After chnaging the copied list it will also change the original list because we have use assignment operator to copy the list
# If we want that original list should not be change then we use copy method

list_org = ["banana", "apple", "mango"]

# copying list using copy method
list_cpy = list_org.copy()

#this will also make copy of the list
list_cpy = list(list_org) 

# third way to copy the list
list_cpy = list_org[:]

list_cpy.append("Orange")

print(list_cpy)
print(list_org)