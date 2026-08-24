class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"{self.name} earns {self.salary}"
emp = Employee("Shabanam", 70000)
print(emp)
'''
Shabanam earns 70000
'''
 
# B. FastAPI Endpoint with Pydantic Request Model
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class EmployeeRequest(BaseModel):
    name: str
    salary: float
@app.post("/employee")
def create_employee(employee: EmployeeRequest):
    return {
        "message": "Employee created",
        "name": employee.name,
        "salary": employee.salary
    }
 
# C. Pandas groupby().agg() Call
import pandas as pd
df = pd.DataFrame({
"name": ["Shabanam", "Arsha", "Reni"],
"department": ["IT", "HR", "IT"],
"salary": [70000, 50000, 75000]
})
summary = (
    df.groupby("department")
      .agg(
          average_salary=("salary", "mean"),
          headcount=("name", "count")
      )
)
print(summary)
"""             average_salary  headcount
department                           
HR                 50000.0          1
IT                 72500.0          2
"""