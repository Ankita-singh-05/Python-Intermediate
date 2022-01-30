# Disjoint set -- both the sets have null intersection or no same elements 

setA = {1,2,3,4,5}
setB = {1,2,3,4}
print(setA.isdisjoint(setB)) #False -- have common elements

setA = {1,2,3,4,5}
setB = {6,7,8}
print(setA.isdisjoint(setB)) #True -- null intersection
