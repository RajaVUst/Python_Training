# Task 6: Object-Oriented Programming, FastAPI, and Pandas Aggregation

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str


@app.post("/users")
def create_user(user: User):
    return user


import pandas as pd

df = pd.DataFrame({
    "department": ["IT", "IT", "HR"],
    "salary": [60000, 65000, 50000]
})

result = df.groupby("department").agg(
    average_salary=("salary", "mean")
)

print(result)

# Mistakes Found:
# None in the class example.
# Initially forgot the decorator @app.post in FastAPI.
# Initially forgot named aggregation syntax in pandas.

# Reasons:
# FastAPI: Syntax recall issue.
# Pandas: Misremembered aggregation format.

# Output:
#            average_salary
# department
# HR               50000.0
# IT               62500.0
