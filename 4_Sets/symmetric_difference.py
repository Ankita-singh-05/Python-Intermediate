# Symmetric difference - It will return all the elements from both the set except the elements which are same in both
# In simple words it returns all the dissimilar elements

setA = {1,2,3,4,5,6,7,8,9,10}
setB = {1,2,3,4,5,11,12}

sym_diff = setA.symmetric_difference(setB)
print(sym_diff)
# {6,7,8,9,10,11,12}

sym_diff = setB.symmetric_difference(setA)
print(sym_diff)
# {6,7,8,9,10,11,12}


