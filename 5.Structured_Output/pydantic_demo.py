from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'nitesh'
    age: Optional[int] = None # Optional
    email: EmailStr # Email Validator
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value of ' \
    'representating the cgpa of the student') # constrains
    # We can add regular expressions as well

new_student = {'age':'32','email':'abc123@gmail.com','cgpa':9} # Typecorsing

student = Student(**new_student) 
# print(student)
# print(dict(student))

# Dictionary extract the value
# student_dict = dict(student)
# print(student_dict['age'])

# JSON
student_json = student.model_dump_json()
