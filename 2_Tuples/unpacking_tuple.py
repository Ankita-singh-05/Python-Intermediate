# Unpacking elements

my_tuple = "Ankita", 23, "Pune"

# if we will assign to only 2 values then it will throw an error
name, age, city = my_tuple

print(name)
print(age)
print(city)

my_tuple2 = (7, 8, 9, 4)
item1, *item2, item3 = my_tuple2

print(item1)
print(item3)
# Remaining elements in the tuple is converted as list
print(item2) 