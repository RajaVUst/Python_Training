class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee(name={self.name}, salary={self.salary})"


emp = Employee("Alice", 75000)
print(emp)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class EmployeeRequest(BaseModel):
    name: str
    department: str

@app.post("/employee")
def create_employee(employee: EmployeeRequest):
    return {
        "message": "Employee created",
        "employee": employee.model_dump()
    }

# mistake 1
# Category: Memory / Syntax
# Issue: I returned the Pydantic model object directly.

# mistake 2 : panda aggregation 
# Category: Concept
# Issue: I initially thought this was the only correct way to calculate headcount.

# mistake 3 : dunder method
# Category: Concept
# Issue: This is valid, but I was unsure whether __str__() or __repr__() was more appropriate.
