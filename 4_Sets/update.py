# UNION, INTERSECTION AND DIFFERENCE does not modify the original set it creates the new set

setA = {1,2,3,4,5,6,7,8,9,10}
setB = {1,2,3,4,5,11,12}

# Update is use to merge the sets without any duplication
setA.update(setB)
print(setA)

