# Exception Handling 
# If try condition is not satisfied then it print the exception block
# Its good practice to specify the type of exception you want to catch

try:
    a = 5 / 0
except:
    print("an error happend")
# an error happend

try:
    a = 5 / 0
except Exception as e:
    print(e)
#division by zero

try:
    a = 5 / 1
    b = a + "10"
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
# unsupported operand type(s) for +: 'float' and 'str'


# Whatever error is catched first is printed
try:
    a = 5 / 0
    b = a + "10"
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
# division by zero

# If no exception occur then we can print the else block
try:
    a = 5 / 1
    b = a + 10
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("Everything is Fine!!")
# Everything is Fine!!

# Finally Clause - It occurs always no matter the exception happens or not 
# Nd it is use to make some cleanup operations
try:
    a = 5 / 1
    b = a + 10
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("Everything is Fine!!")
finally:
    print("cleaning up!")
# Everything is Fine!!
# cleaning up!
