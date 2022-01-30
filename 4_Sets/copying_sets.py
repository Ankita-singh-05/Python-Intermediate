setA = {1,2,3,4,5,6}

setB = setA
print(setB)

# if we will modify the setB then setA will also change
setB.add(7)
print(setA)

# To make the actual copy 
# By using copy method the changes are made to copy set only

setA = {1,2,3,4,5,6}
setB = setA.copy()
print(setB)
setB.add(7)
print(setA)

# Another way for actual copy
setA = {1,2,3,4,5,6}
setB = set(setA)
print(setB)
