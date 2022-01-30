# Symmetric Difference -- It prints the all the elements from both the sets except the common elements

setA = {1,2,3,4,5,6,7,8,9,10}
setB = {1,2,3,4,5,11,12}

setA.symmetric_difference_update(setB)
print(setA)
# {6,7,8,9,10,11,12} --remaining are common elements

setB.symmetric_difference_update(setA)
print(setB)
# {6,7,8,9,10,11,12}