# 1. OOP — Class with constructor and one dunder method

class TrainingRun:
    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate

    def __str__(self):
        return f"TrainingRun(model='{self.model_name}', lr={self.learning_rate})"


run = TrainingRun("gpt-mini", 0.01)

print(run)


# 2. FastAPI — Endpoint with Pydantic request model

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Employee(BaseModel):
    name: str
    department: str
    salary: float


@app.post("/employees")
def create_employee(employee: Employee):
    return {
        "message": "Employee created successfully",
        "employee": employee
    }


# 3. Pandas — groupby().agg()

import pandas as pd

employees = pd.DataFrame({
    "name": ["Alice", "Bob", "Carol", "David"],
    "department": ["Engineering", "HR", "Engineering", "Sales"],
    "salary": [75000, 55000, 82000, 60000]
})

summary = employees.groupby("department").agg(
    average_salary=("salary", "mean"),
    headcount=("name", "count")
)

print(summary)


# 4. Mistake Review

# Mistake 1:
# Category: Syntax
# Explanation: I forgot the correct syntax for defining a Pydantic
# model field using a type hint.


# Mistake 2:
# Category: Typo
# Explanation: I accidentally typed "grouby" instead of "groupby".


# Mistake 3:
# Category: Concept
# Explanation: I initially confused Pydantic's BaseModel with a normal
# Python class and did not understand that FastAPI uses it to validate
# incoming request data.




# TrainingRun(model='gpt-mini', lr=0.01)
#              average_salary  headcount
# department                            
# Engineering         78500.0          2
# HR                  55000.0          1
# Sales               60000.0          1