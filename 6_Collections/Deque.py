# Deque - Deque is a double ended queue.
# It can be use to add or remove elements from both end.
# and both are implemented in a way that it will be very efficiently
from collections import deque

d = deque()
d.append(1)
d.append(2)
print(d)
# deque([1, 2])

d.appendleft(3)
print(d) # deque([3, 1, 2])

# to remove last element
d.pop()
print(d) # deque([3, 1])

# To remove the first element
d.popleft()
print(d) # deque([1])

# To remove all the elements
d.clear()
print(d) # deque([])

d = deque()
d.append(1)
d.append(2)
print(d)

# Extend will add the elements to the right
d.extend([3,4,5])
print(d) # deque([1, 2, 3, 4, 5])

# Extendleft will add the elements to the left
d.extendleft([0,-1,-2])
print(d) # deque([-2, -1, 0, 1, 2, 3, 4, 5])

# Rotate -- it will rotate the elements by 1 place
d.rotate(1)
print(d) # deque([5, -2, -1, 0, 1, 2, 3, 4])

# To rotate to left side
d.rotate(-1)
print(d) # deque([-2, -1, 0, 1, 2, 3, 4, 5])