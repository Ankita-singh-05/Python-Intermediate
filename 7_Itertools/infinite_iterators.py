from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i == 15:
        break

# This make an endless loop starting with 10 if we will not give the break

a = [1,2,3]
for i in cycle(a):
    print(i)
    if i == 2:
        break
# It will cycle the list again and again until break statement is given


# It will repeat 1 infinitely
for i in repeat(1, 4):
    print(i)