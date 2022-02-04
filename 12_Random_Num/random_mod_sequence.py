# Random Module 
import random

mylist = list("ABCDEFGHI")

a = random.sample(mylist, 3)
print(a)
# ['F', 'D', 'C']

a = random.choices(mylist, k=3)
print(a)
# ['E', 'A', 'G']

# Used to shuffle the elements in the list
random.shuffle(mylist)
print(mylist)
# ['F', 'B', 'G', 'H', 'C', 'A', 'I', 'E', 'D']