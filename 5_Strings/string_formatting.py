# There are 4 ways to format the string
# %, .format, f-strings

# For string valur %s is used
var = "Ankita"
my_string = "the variable is %s" %var
print(my_string)

# for integer or decimal value %d is used
var = 3
my_string = "the variable is %d" %var
print(my_string)

# If varibale is floating value and u have pass %d then decimal points are not printed
# var = 3.35456
# my_string = "the variable is %d" %var
# print(my_string) -- 3


# For floating value -- by default 6 decimal points are considered
var = 3.35456
my_string = "the variable is %f" %var
print(my_string) 

var = 3.35456
my_string = "the variable is %.2f" %var
print(my_string) #the variable is 3.35


# .format method =============
my_string = "the variable is {} ".format(var)
print(my_string)
my_string = "the variable is {:.2f} ".format(var)
print(my_string) #the variable is 3.35 

var2 = 6
my_string = "the variable is {:.2f} and {} ".format(var, var2)
print(my_string)


# f-strings
my_string = f"the variable is {var*2} and {var2}"
print(my_string)