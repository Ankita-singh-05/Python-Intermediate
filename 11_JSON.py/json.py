# JSON - Stands for JavaScript Object Notation
# Its a lightweight data format that is used for data exchange.
# It is heavily used in web applications
# Python comes with built in JS module
import json

person = {
    "name": "John", 
    "age": 30, 
    "city": "New York", 
    "hasChildren": False, 
    "titles": ["engineer", "programmer"]
}

personJSON = json.dumps(person)
print(personJSON)

# {"name": "John", "age": 30, "city": "New York", "hasChildren": false, "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4)
print(personJSON)
"""
{
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": false,
    "titles": [
        "engineer",
        "programmer"
    ]
}
"""

# Not recommended
personJSON = json.dumps(person, indent=4, separators=("; ", "= "))
print(personJSON)
"""
{
    "name"= "John";
    "age"= 30;
    "city"= "New York";
    "hasChildren"= false;
    "titles"= [
        "engineer";
        "programmer"
    ]
}
"""