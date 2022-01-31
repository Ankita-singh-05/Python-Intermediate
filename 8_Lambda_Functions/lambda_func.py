# Lambda function -- it is small one line anonymous function that is defined without a name
# It is simple function that is used only once in a code
# Or it is used to higher order functions, meaning functions that take in other func as arg
# Syntax - 
# lambda arguments: expression

add10 = lambda x: x + 10
print(add10(2)) # 12

def add10_func(x):
    return x + 10

mult = lambda x, y : x * y
print(mult(2,3)) # 6