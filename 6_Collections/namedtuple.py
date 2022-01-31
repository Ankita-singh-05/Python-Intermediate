# Namedtuple - it is easy to create and light weight object type, similar to a struct

from collections import namedtuple

Point = namedtuple("Point", "x,y") #This will create a class with field x and y
pt = Point(1, -4)
print(pt)
# Point(x=1, y=-4)

# Accessing the field
print(pt.x) # 1
print(pt.y) # -4