import pandas as pd
import numpy as np

# --------------------------------------------------
# Employee data
# --------------------------------------------------

employees = pd.DataFrame({
    "name": [
        "Amit", "Rahul", "Priya", "Neha",
        "Arjun", "Sneha", "Vikram", "Pooja",
        "Rohan", "Anjali", "Karan", "Meera",
        "Raj", "Simran", "Dev", "John"
    ],

    "department": [
        "IT", "IT", "HR", "HR",
        "Finance", "Finance", "IT", "Sales",
        "Sales", "HR", "Finance", "IT",
        "Sales", "Finance", "IT", "Marketing"
    ],

    "salary": [
        60000, 70000, 50000, 55000,
        75000, 80000, 65000, 45000,
        50000, 52000, 85000, 72000,
        48000, 78000, 68000, 50000
    ],

    "years_experience": [
        2, 4, 3, 5,
        6, 7, 3, 2,
        4, 3, 8, 5,
        2, 7, 4, 1
    ]
})


# --------------------------------------------------
# Department data
# --------------------------------------------------

departments = pd.DataFrame({
    "department": [
        "IT",
        "HR",
        "Finance",
        "Sales"
    ],

    "department_budget": [
        500000,
        250000,
        600000,
        300000
    ]
})


# --------------------------------------------------
# 1. Inner join
# --------------------------------------------------

inner_join = pd.merge(
    employees,
    departments,
    on="department",
    how="inner"
)

print("INNER JOIN:")
print(inner_join)


# Output:
# John from Marketing is NOT present because
# Marketing does not exist in departments.


# --------------------------------------------------
# 2. Left join
# --------------------------------------------------

left_join = pd.merge(
    employees,
    departments,
    on="department",
    how="left"
)

print("\nLEFT JOIN:")
print(left_join)


# Output:
# John ... Marketing ... NaN
#
# The department_budget for Marketing is NaN
# because Marketing does not exist in departments.


# --------------------------------------------------
# 3. Introduce missing values
# --------------------------------------------------

employees.loc[2, "salary"] = np.nan
employees.loc[7, "years_experience"] = np.nan

print("\nMissing values:")
print(employees.isna().sum())


# Output:
# name                0
# department          0
# salary              1
# years_experience    1
# dtype: int64


# --------------------------------------------------
# 4. Handle missing values
# --------------------------------------------------

# Salary is numeric, so using the mean preserves the
# employee row instead of unnecessarily deleting it.
employees["salary"] = employees["salary"].fillna(
    employees["salary"].mean()
)

# Years of experience is also numeric. We use the median
# because experience can be skewed by a few senior employees.
employees["years_experience"] = employees[
    "years_experience"
].fillna(
    employees["years_experience"].median()
)

print("\nAfter handling missing values:")
print(employees.isna().sum())


# Output:
# name                0
# department          0
# salary              0
# years_experience    0
# dtype: int64