def start_end_decorator(func):

    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper


def print_name():
    print("Ankita")

print_name()
# Ankita

# In order to apply the decorator
print_name = start_end_decorator(print_name) 
# upper line does the same thing as @start_end_decorator
print_name()
# Start
# Ankita
# End

@start_end_decorator
def print_name():
    print("Ankita")
print_name()
# Start
# Ankita
# End


@start_end_decorator
def add5(x):
    return x + 5
add5(10)
# Start
# End
# If we have to pass the argument in thhe function then we need to define the ars and **kwargs as an argument
result = add5(10)
print(result)
# None 
# It will return the result after -- result = func(*args, **kwargs)
# 15
