# Demonstrate readiness via a short quiz/coding test
class Student:
    def __init__(self, name):
        self.name = name
 
    def __str__(self):
        return self.name
 
student = Student("Lokesh")
print(student)
 
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class Student(BaseModel):
    name: str
    age: int
 
@app.post("/student")
def create_student(student: Student):
    return student
 
 
import pandas as pd
data = {
    "department": ["IT", "IT", "HR", "HR"],
    "salary": [50000, 60000, 40000, 45000]
}
 
df = pd.DataFrame(data)
result = df.groupby("department").agg(
    average_salary=("salary", "mean"),
    employee_count=("salary", "count")
)
print(result)
 
 
# Output:
# Lokesh
#             average_salary  employee_count
# department                                
# HR                 42500.0               2
# IT                 55000.0               2