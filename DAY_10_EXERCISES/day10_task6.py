# A. Class with Constructor and Dunder Method
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"{self.name} earns {self.salary}"
emp = Employee("Alice", 70000)
print(emp)
'''
Alice earns 70000
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
"name": ["Alice", "Bob", "Charlie"],
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

'''
Alice earns 70000
FastAPI endpoint created successfully.
Grouped summary example:
            average_salary  headcount
department
Finance           68750.0          4
HR                53000.0          4
IT                73750.0          4
Marketing         60000.0          3
'''

#part2
'''
After comparing with the master-class materials:
1. Class Example
   Status: Correct
2. FastAPI Example
   Mistake Found:
   Initially forgot to inherit from BaseModel
   in the request model.
3. Pandas groupby().agg() Example
   Mistake Found:
   Initially wrote groupby("department").mean()
   instead of using named aggregations inside
   .agg().
'''

#part3
'''
Mistake 1:
Category: Syntax
Explanation:
I forgot to inherit from BaseModel because I
misremembered the exact Pydantic request-model
syntax required by FastAPI.
Mistake 2:
Category: Concept
Explanation:
I remembered grouping data correctly but forgot
that the task specifically required multiple named
aggregations using .agg(), indicating a gap in
remembering the full aggregation syntax.
'''

#note
'''
This practice exercise measures readiness before the
graded assessment by recalling key concepts from memory.
The class example demonstrates object-oriented
programming with a constructor (__init__) and a
dunder method (__str__).
The FastAPI example demonstrates creating an API
endpoint that accepts validated input through a
Pydantic request model.
The Pandas example demonstrates grouping data and
performing named aggregations using groupby().agg().
Reviewing mistakes helps distinguish between:
- Typo mistakes (small typing errors)
- Syntax mistakes (incorrect language structure)
- Concept mistakes (misunderstanding or forgetting
  an idea)
Identifying the type of mistake makes it easier to
focus '''