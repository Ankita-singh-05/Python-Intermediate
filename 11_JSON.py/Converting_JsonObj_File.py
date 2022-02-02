import json

person = {
    "name": "John", 
    "age": 30, 
    "city": "New York", 
    "hasChildren": False, 
    "titles": ["engineer", "programmer"]
}

# Person.json file will be created with all the above objects in it

with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

