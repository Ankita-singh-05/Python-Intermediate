import functools

def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

print(help(add5))
print(add5.__name__)

# Help on function wrapper in module __main__:

# wrapper(*args, **kwargs)

# None
# wrapper
# ----------------------------------------------------------------
# After adding functools wrapper
# Help on function add5 in module __main__:

# add5(x)

# None
# add5