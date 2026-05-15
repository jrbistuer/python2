"""
DICTIONARIES
Dictionaries are a collection of key-value pairs. They are unordered, mutable, and indexed.
Dictionaries are defined using curly braces {} and key-value pairs are separated by a colon :.
Dictionaries are very useful for storing and retrieving data based on keys. 
They are commonly used in various applications such as databases, APIs, and data manipulation.
"""

user1 = {
    "name": "John",
    "surname": "Doe",
    "email": "john.doe@example.com",
    "age": 30,
    "city": "New York"
}

print(user1)  # Printing the entire dictionary
print(user1["name"])  # Accessing a value using its key
# print(user1.email)  # This will raise an AttributeError ERROR because dictionaries do not support attribute access
print(user1.get("email"))  # Accessing a value using the get method
print(user1.get("country")) # Accessing a value that does not exist will return None
print(user1.get("country", "USA"))  # Accessing a value with a default value if the key does not exist

user1["age"] = 31  # Modifying an existing value
print(user1)
user1["country"] = "USA"  # Adding a new key-value pair
print(user1)
del user1["city"]  # Removing a key-value pair
print(user1)

user1.pop("email")  # Removing a key-value pair using pop method
print(user1)
user1.pop("country", "Key not found")  # Removing a key-value pair with a default value if the key does not exist

print(user1.keys())  # Getting all the keys in the dictionary
print(user1.values())  # Getting all the values in the dictionary

for key in user1:  # Iterating over the keys in the dictionary
    print(key)

for key, value in user1.items():  # Iterating over the key-value pairs in the dictionary
    print(f"{key}: {value}")

# checking if a key exists in the dictionary
print("name" in user1)  # Checking if the key "name" exists in the dictionary
print("email" in user1)  # Checking if the key "email" exists in the dictionary

print(len(user1))  # Getting the number of key-value pairs in the dictionary

print(user1)  # Printing the entire dictionary
user2 = user1 # Assigning user1 to user2 creates a reference to the same dictionary, not a copy
print(user2)  # Printing the entire dictionary
user2["name"] = "Jane" 
print(user1)  # Printing the entire dictionary
print(user2)  # Printing the entire dictionary
user3 = user1.copy()  # Creating a copy of the dictionary
print(user3)  # Printing the entire dictionary
user3["name"] = "Alice"
print(user1)  # Printing the entire dictionary
print(user2)  # Printing the entire dictionary
print(user3)  # Printing the entire dictionary
user2["name"] = "Bob"
print(user1)  # Printing the entire dictionary
print(user2)  # Printing the entire dictionary
print(user3)  # Printing the entire dictionary

import copy
user4 = copy.deepcopy(user1)  # Creating a deep copy of the dictionary
# the difference between copy and deepcopy is that deepcopy will create a new dictionary with new objects
# for all the values, while copy will create a new dictionary with references to the same objects for the values.
# This means that if the values in the dictionary are mutable objects (like lists or other dictionaries),
# modifying them in one dictionary will affect the other dictionary if you use copy, but not if you use deepcopy.
print(user4)  # Printing the entire dictionary
user4["name"] = "Charlie"
print(user1)  # Printing the entire dictionary
print(user2)  # Printing the entire dictionary
print(user3)  # Printing the entire dictionary
print(user4)  # Printing the entire dictionary

user = {
    "name": "John",
    "surname": "Doe",
    "email": "john.doe@example.com",
    "age": 30,
    "city": "New York"
}

print(user)  # Printing the entire dictionary
user["name"] = "Jane"  # Modifying an existing value
print(user)  # Printing the entire dictionary
user["country"] = "USA"  # Adding a new key-value pair
print(user)  # Printing the entire dictionary

from typing import TypedDict, Optional
class User(TypedDict):
    name: str
    surname: str
    email: str
    age: int
    city: str
    country: Optional[str]

user_typed: User = {
    "name": "John",
    "surname": "Doe",
    "email": "john.doe@example.com",
    "age": 30,
    "city": "New York",
    "country": None
}
# user1["country"] = "USA"  # Modifying an existing value

