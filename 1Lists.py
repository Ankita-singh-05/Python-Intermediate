# Lists are ordered, mutable, and it allows duplicate elements

from operator import ne


myList = ["apply", "banana", "cherry"]
print(myList)

# Empty List
# myList2 = list()
# print(myList2)

# List elements can be of any data type
myList = [2, True, "Ankita"]
print(myList)

# Access the element of the list
# print(myList[0])  --> print the first element
# print(myList[-1])  --> print the last element

# for i in myList:
#     print(i)

# To check if the elements are present in the list or not
if "banana" in myList:
    print("Yes")
else:
    print("No")

# To check the length of the list
print(len(myList))

# To insert the item in the list
myList.append("Anjali")   # it will add the element to the last of the list
print(myList)
myList.insert(3, "Yash")  #it will add the element to the index which u have assign to it
print(myList)

# To remove the items
myList.pop()
print(myList)

myList.remove(1)
print(myList)

"""
===========================================================
  To remove all the elements
===========================================================
myList.clear()
print(myList)
"""

# ===========================================================
#   To reverse the elements
# ===========================================================
myList.reverse()
print(myList)


num_list = [2, 1, 0, -1, 5, 7, 6]
# ===========================================================
#   To sort the list
# ===========================================================
num_list.sort()
print(num_list)

# ===========================================================
#   New list with same value multiple times
# ===========================================================

new_list1 = [0] * 5
new_list2 = [1,2,3,4,5]
new_list = new_list1 + new_list2
print(new_list)


