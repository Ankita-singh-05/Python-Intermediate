# difference - it will not take the elements present in the other set 
setA = {1,2,3,4,5,6,7,8,9,10}
setB = {1,2,3,4,5,11,12}

diff = setA.difference(setB)
print(diff)
# {6,7,8,9,10}

diff = setB.difference(setA)
print(diff)
# {11,12} - because except 11,12 all the other elements are present in the setA