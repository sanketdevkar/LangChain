from typing import TypedDict # Import TypedDict to create dictionary types with specific keys and value types

class Person(TypedDict): # Define a Person TypedDict type

    name: str # The 'name' key must map to a string
    age: int # The 'age' key must map to an integer

new_person: Person = {'name':'nitish', 'age':35} # Create a dictionary matching the Person type

print(new_person) # Print the created dictionary