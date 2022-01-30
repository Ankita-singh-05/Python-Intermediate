# Difference update -- It updates the element by removing the elements found in another set

setA = {1,2,3,4,5,6,7,8,9,10}
setB = {1,2,3,4,5,11,12}


setA.difference_update(setB)
print(setA)
# {6,7,8,9,10} -- print the elements by removing the same element present in other set

setB.difference_update(setA)
print(setB)
# {11,12} -- reamining elements are present in setB
