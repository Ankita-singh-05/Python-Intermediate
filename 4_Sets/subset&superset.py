# Subset means all the elements in the first set are also in second set

setA = {1,2,3,4,5}
setB = {1,2,3,4}

print(setA.issubset(setB)) #False

setA = {1,2,3,4,5}
setB = {1,2,3,4}
print(setB.issubset(setA)) #True -- because all the elements of setB are present in setA

# Superset-- all the elemets of second set should be present in first set
setA = {1,2,3,4,5}
setB = {1,2,3,4}
print(setA.issuperset(setB)) #True

setA = {1,2,3,4,5}
setB = {1,2,3,4}
print(setB.issuperset(setA)) #False- because setB does not conatin 5