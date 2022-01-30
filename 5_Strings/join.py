from timeit import default_timer as timer

my_list = ["a"] * 6
print(my_list)

# Bad method
start = timer()
my_string = ""
for i in my_list:
    my_string += i
print(my_string) #aaaaaa
stop = timer()
print(stop - start)

# Good
start = timer()
my_string = "".join(my_list)
print(my_string) #aaaaaa
stop = timer()
print(stop - start)

# Join method is much more faster it takes less time than the first method 
