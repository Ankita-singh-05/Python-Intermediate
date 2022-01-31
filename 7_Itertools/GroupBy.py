# Groupby function - it makes an iterator that returns keys and groups from iterable

from itertools import groupby

def smaller_than_3(x):
    return x < 3

a= [1,2,3,4]
group_obj = groupby(a, key= smaller_than_3)
# group_obj = groupby(a, key= lambda x : x < 3) -- this is same as above
for key, value in group_obj: 
        print(key, list(value))
        # True [1, 2]
        # False [3, 4]


persons = [{"name": "Ankita", "age": 20}, {"name": "Yash", "age": 10},
            {"name": "Anjali", "age": 19}, {"name": "Komal", "age": 17}]

group_obj = groupby(persons, key=lambda x: x["age"])
for key, value in group_obj:
    print(key, list(value))

""" if the age is same then it will group in same list
20 [{'name': 'Ankita', 'age': 20}]
10 [{'name': 'Yash', 'age': 10}]
19 [{'name': 'Anjali', 'age': 19}]
17 [{'name': 'Komal', 'age': 17}]
"""