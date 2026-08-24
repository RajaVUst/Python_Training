# Q1
import numpy as np

prices = [
    10, 20, 30, 40, 50,
    60, 70, 80, 90, 100,
    110, 120, 130, 140, 150,
    160, 170, 180, 190, 200
]

taxed_prices_loop = []

for price in prices:
    taxed_prices_loop.append(price * 1.08)

prices_array = np.array(prices)

taxed_prices_vectorized = prices_array * 1.08

threshold = 50
filtered_prices = taxed_prices_vectorized[taxed_prices_vectorized > threshold]

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print(taxed_prices_loop)
print(taxed_prices_vectorized)
print(filtered_prices)
print(matrix.sum(axis=1))
print(matrix.sum(axis=0))

# Q2
import pandas as pd

employees = pd.DataFrame({
    "name": [
        "Alice", "Bob", "Carol", "David", "Eva",
        "Frank", "Grace", "Helen", "Ian", "Jack",
        "Kevin", "Linda", "Mary", "Nick", "Olivia"
    ],
    "department": [
        "IT", "HR", "IT", "Finance", "HR",
        "IT", "Finance", "HR", "IT", "Finance",
        "IT", "HR", "Finance", "IT", "HR"
    ],
    "salary": [
        60000, 45000, 70000, 55000, 48000,
        75000, 62000, 47000, 72000, 68000,
        78000, 50000, 65000, 74000, 52000
    ],
    "years_experience": [
        5, 2, 7, 4, 3,
        8, 6, 2, 7, 5,
        9, 3, 6, 8, 4
    ]
})

employees.to_csv("employees.csv", index=False)

df = pd.read_csv("employees.csv")

print(df.info())
print(df.describe())

it_employees = df[df["department"] == "IT"]
query_employees = df.query("department == 'IT'")

print(it_employees)
print(query_employees)

summary = (
    df.groupby("department")
      .agg(
          average_salary=("salary", "mean"),
          headcount=("name", "count")
      )
      .sort_values(
          by="average_salary",
          ascending=False
      )
)

print(summary)

# Q3
departments = pd.DataFrame({
    "department": ["IT", "HR", "Finance"],
    "department_budget": [500000, 250000, 400000]
})

inner_join = pd.merge(
    df,
    departments,
    on="department",
    how="inner"
)

print(inner_join)

new_employee = pd.DataFrame({
    "name": ["Sam"],
    "department": ["Legal"],
    "salary": [50000],
    "years_experience": [3]
})

df = pd.concat(
    [df, new_employee],
    ignore_index=True
)

left_join = pd.merge(
    df,
    departments,
    on="department",
    how="left"
)

print(left_join)

df.loc[1, "salary"] = np.nan
df.loc[3, "years_experience"] = np.nan

print(df.isna().sum())

df["salary"].fillna(
    df["salary"].mean(),
    inplace=True
)

df["years_experience"].fillna(
    df["years_experience"].mean(),
    inplace=True
)

print(df)

# Q4
import matplotlib.pyplot as plt

avg_salary = (
    df.groupby("department")["salary"]
    .mean()
)

avg_salary.plot(kind="bar")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()

plt.scatter(
    df["years_experience"],
    df["salary"]
)

plt.title("Experience vs Salary")
plt.xlabel("Years Experience")
plt.ylabel("Salary")
plt.show()

plt.hist(df["salary"], bins=8)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# Bar chart compares values between departments.
# Scatter plot shows relationship between experience and salary.
# Histogram shows salary distribution.

# Q5
# OOP:
# Had to move away from writing getters/setters for everything.

# FastAPI:
# Relied on Pydantic models instead of manual validation.

# Pandas/NumPy:
# Learned to use vectorized operations instead of loops.

# DataFrame filtering will be useful in ML projects
# for cleaning, preparing and selecting data before
# model training.

# Least confident topic:
# Advanced Pandas merging.

# Action:
# Practice additional merge and join exercises.

# Q6

# Class with constructor and dunder method
class Employee:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


# FastAPI endpoint with Pydantic model
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str

@app.post("/users")
def create_user(user: User):
    return user


# Pandas groupby aggregation
grouped = (
    df.groupby("department")
      .agg(
          average_salary=("salary", "mean"),
          employee_count=("name", "count")
      )
)

print(grouped)
