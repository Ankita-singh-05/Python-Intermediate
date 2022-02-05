def start_end_decorator(func):

    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper


def print_name():
    print("Ankita")

print_name()
# Ankita

# In order to apply the decorator
print_name = start_end_decorator(print_name)
# Start
# Ankita
# End

# 3.18