# Slicing in Python ---> its a very effective method to access elements from the list

myList = [1,2,3,4,4,5,6,7,8,9,0]

print(myList[1:5]) #it will exclude the last element

# It will print all the elements from index 1 to end of the list
print(myList[1:])

# Step index
print(myList[::]) #it will print all the elements
print(myList[::2]) #it will print every 2nd elements
print(myList[::3]) #it will print every 3rd elements

# we can reverse the list by -ve step indexing
print(myList[::-1])
print(myList[1:6:2])