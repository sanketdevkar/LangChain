from pydantic import BaseModel, EmailStr, Field # Import Pydantic tools for data validation and model definition
from typing import Optional # Import Optional for fields that can be None

class Student(BaseModel): # Define a Pydantic model for a Student

    name: str = 'nitish' # A string field with a default value of 'nitish'
    age: Optional[int] = None # An optional integer field with a default value of None
    email: EmailStr # A required field that must be a valid email address string
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student') # A float field constrained between 0 and 10, defaulting to 5


new_student = {'age':'32', 'email':'abc@gmail.com'} # Create a dictionary with student data (age will be cast to int by Pydantic)

student = Student(**new_student) # Instantiate the Student model, unpacking the dictionary to validate and populate fields

student_dict = dict(student) # Convert the Pydantic model instance back into a standard Python dictionary

print(student_dict['age']) # Print the validated 'age' value

student_json = student.model_dump_json() # Serialize the Pydantic model instance into a JSON string