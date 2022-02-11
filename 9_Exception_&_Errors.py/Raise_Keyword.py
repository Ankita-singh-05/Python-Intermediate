# Raise -- If we want to force an exception to occur when a certain condition is met, then we can do this  with the raise keyword

x = -5
if x < 0:
    raise Exception("x should be +ve")

# If condition is true then error is not shown
x = 5
if x < 0:
    raise Exception("x should be +ve")
