# ============================================================
# MASTER CLASS 6
# NumPy, Pandas, Visualization & Readiness Check
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# TASK 1 - VECTORIZE IT
# ============================================================

print("\n" + "=" * 60)
print("TASK 1 - NUMPY FUNDAMENTALS")
print("=" * 60)

# 20 product prices
prices = [
    20, 25, 30, 35, 40,
    45, 50, 55, 60, 65,
    70, 75, 80, 85, 90,
    95, 100, 110, 120, 150
]

# 1. Loop-based version
taxed_prices_loop = []

for price in prices:
    taxed_prices_loop.append(price * 1.08)

print("\nTaxed prices using loop:")
print(taxed_prices_loop)


# 2. NumPy vectorized version
prices_array = np.array(prices)

taxed_prices_numpy = prices_array * 1.08

print("\nTaxed prices using NumPy:")
print(taxed_prices_numpy)


# Check both results are the same
print("\nBoth results are identical:")
print(np.allclose(taxed_prices_loop, taxed_prices_numpy))


# 3. Boolean masking
threshold = 50

above_threshold = taxed_prices_numpy[taxed_prices_numpy > threshold]

print("\nTaxed prices above 50:")
print(above_threshold)


# 4. 2D NumPy array
numbers = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

row_sums = numbers.sum(axis=1)
column_sums = numbers.sum(axis=0)

print("\n2D Array:")
print(numbers)

print("\nRow sums:")
print(row_sums)

print("\nColumn sums:")
print(column_sums)


# ============================================================
# TASK 2 - LOAD & EXPLORE
# ============================================================

print("\n" + "=" * 60)
print("TASK 2 - PANDAS ESSENTIALS")
print("=" * 60)


# Create employee data
employee_data = {
    "name": [
        "Arun", "Bala", "Charan", "Deepa", "Elena",
        "Farhan", "Gokul", "Hari", "Isha", "Jaya",
        "Karthik", "Latha", "Manoj", "Nisha", "Praveen"
    ],

    "department": [
        "IT", "HR", "Finance", "IT", "HR",
        "Finance", "IT", "Sales", "Sales", "HR",
        "Finance", "IT", "Sales", "Finance", "IT"
    ],

    "salary": [
        60000, 45000, 55000, 70000, 50000,
        65000, 75000, 48000, 52000, 47000,
        68000, 72000, 58000, 62000, 80000
    ],

    "years_experience": [
        2, 3, 4, 5, 2,
        6, 7, 3, 4, 2,
        7, 6, 5, 4, 8
    ]
}

employees = pd.DataFrame(employee_data)

# Save as CSV
employees.to_csv("employees.csv", index=False)

# 1. Read CSV
df = pd.read_csv("employees.csv")

print("\nEmployee Data:")
print(df)

print("\nDataFrame Info:")
df.info()

print("\nDataFrame Description:")
print(df.describe())


# 2. Filter using boolean indexing
it_employees_boolean = df[df["department"] == "IT"]

print("\nIT employees using boolean indexing:")
print(it_employees_boolean)


# Filter using query()
it_employees_query = df.query("department == 'IT'")

print("\nIT employees using query():")
print(it_employees_query)


# Check both results are the same
print("\nBoth filtering methods give the same result:")
print(it_employees_boolean.reset_index(drop=True).equals(
    it_employees_query.reset_index(drop=True)
))


# 3. Group by department and aggregate
summary = df.groupby("department").agg(
    average_salary=("salary", "mean"),
    headcount=("name", "count")
)

# 4. Sort by average salary
summary = summary.sort_values(
    "average_salary",
    ascending=False
)

print("\nDepartment Summary:")
print(summary)


# ============================================================
# TASK 3 - JOIN THE DATA
# ============================================================

print("\n" + "=" * 60)
print("TASK 3 - MERGING & MISSING DATA")
print("=" * 60)


# Create departments DataFrame
departments = pd.DataFrame({
    "department": ["IT", "HR", "Finance", "Sales"],
    "department_budget": [500000, 250000, 400000, 300000]
})

print("\nDepartments:")
print(departments)


# 1. Inner join
inner_join = pd.merge(
    df,
    departments,
    on="department",
    how="inner"
)

print("\nInner Join:")
print(inner_join)


# 2. Add employee with unknown department
new_employee = pd.DataFrame({
    "name": ["Rahul"],
    "department": ["Marketing"],
    "salary": [55000],
    "years_experience": [3]
})

df_with_unknown = pd.concat(
    [df, new_employee],
    ignore_index=True
)

# Left join
left_join = pd.merge(
    df_with_unknown,
    departments,
    on="department",
    how="left"
)

print("\nLeft Join with unmatched department:")
print(left_join)

print("\nRahul's row:")
print(left_join[left_join["name"] == "Rahul"])


# 3. Introduce missing values
df_missing = df.copy()

df_missing.loc[2, "salary"] = np.nan
df_missing.loc[7, "years_experience"] = np.nan

print("\nData with missing values:")
print(df_missing)


print("\nMissing values:")
print(df_missing.isna().sum())


# 4. Handle missing values
# Salary is filled with the mean because salary is numeric
# and using the mean allows us to keep the employee record.
df_missing["salary"] = df_missing["salary"].fillna(
    df_missing["salary"].mean()
)

# Years of experience is also filled with its mean
# so that we do not lose the employee row.
df_missing["years_experience"] = df_missing["years_experience"].fillna(
    df_missing["years_experience"].mean()
)

print("\nAfter handling missing values:")
print(df_missing)

print("\nMissing values after handling:")
print(df_missing.isna().sum())


# ============================================================
# TASK 4 - TELL A STORY
# ============================================================

print("\n" + "=" * 60)
print("TASK 4 - VISUALIZATION")
print("=" * 60)


# Use the cleaned DataFrame
clean_df = df_missing.copy()


# 1. Bar chart - Average salary by department
average_salary = clean_df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))

average_salary.plot(kind="bar")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.tight_layout()
plt.show()

print(
    "\nBar chart question: "
    "Which department has the highest or lowest average salary?"
)


# 2. Scatter plot - Experience vs Salary
plt.figure(figsize=(8, 5))

for department in clean_df["department"].unique():

    department_data = clean_df[
        clean_df["department"] == department
    ]

    plt.scatter(
        department_data["years_experience"],
        department_data["salary"],
        label=department
    )

plt.title("Years of Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()

plt.tight_layout()
plt.show()

print(
    "\nScatter plot question: "
    "Is there a relationship between years of experience and salary?"
)


# 3. Histogram - Salary distribution
plt.figure(figsize=(8, 5))

plt.hist(clean_df["salary"], bins=5)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.show()

print(
    "\nHistogram question: "
    "How are employee salaries distributed across different salary ranges?"
)


# ============================================================
# TASK 5 - CONSOLIDATION REFLECTION
# ============================================================


print("\n" + "=" * 60)
print("TASK 6 - READINESS SELF-CHECK")
print("=" * 60)


# 1A. OOP - Class with constructor and dunder method

class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


student = Student("Arun")

print("\nOOP Example:")
print(student)


# 1B. FastAPI + Pydantic example

# Example code written from memory:

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    name: str
    age: int


@app.post("/users")
def create_user(user: User):
    return {
        "name": user.name,
        "age": user.age
    }


print("\nFastAPI + Pydantic example created successfully.")


# 1C. Pandas groupby().agg()

grouped_data = df.groupby("department").agg(
    average_salary=("salary", "mean"),
    headcount=("name", "count")
)

print("\nPandas groupby().agg() example:")
print(grouped_data)


# 2. Mistake checking
print("""
Mistake Check:

OOP:
No major mistake. The class uses __init__ as the constructor
and __str__ as a dunder method.

FastAPI:
No major mistake. The Pydantic model is used as the request
body and the endpoint receives the validated model.

Pandas:
No major mistake. groupby().agg() uses named aggregations
for average salary and headcount.
""")


# 3. Categorized explanation
print("""
Mistake Categories:

Typo:
A typo happens when the concept is known but a name or character
is typed incorrectly.

Syntax:
A syntax mistake happens when Python syntax is remembered
incorrectly.

Concept:
A conceptual mistake happens when the purpose or behavior of
a feature is not fully understood.

In this practice attempt, no major conceptual mistakes were found.
""")


# ============================================================
# FINAL MESSAGE
# ============================================================
