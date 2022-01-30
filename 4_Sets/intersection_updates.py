# Intersection updates keep the value which is present in both the sets

setA = {1,2,3,4,5,6,7,8,9,10}
setB = {1,2,3,4,5,11,12}

setA.intersection_update(setB)
print(setA)
# {1,2,3,4,5} -- common elements in both the sets

setB.intersection_update(setA)
print(setB)