import pandas as  pd
from pathlib import Path

import numpy as np

employees = pd.read_csv(
    Path(__file__).resolve().parents[1] / "employees.csv"
)

departments = pd.DataFrame({
    "department": ["IT", "HR", "Finance"],
    "department_budget": [
        1000000,
        500000,
        1500000
    ]
})

# 1. Inner Join
inner_join = pd.merge(
    employees,
    departments,
    on="department",
    how="inner"
)

print("INNER JOIN")
print(inner_join.head())

# 2. Unmatched employee
new_employee = pd.DataFrame({
    "name": ["Zara"],
    "department": ["Marketing"],
    "salary": [65000],
    "years_experience": [4]
})

employees_extended = pd.concat(
    [employees, new_employee],
    ignore_index=True
)

left_join = pd.merge(
    employees_extended,
    departments,
    on="department",
    how="left"
)

print("\nLEFT JOIN")
print(left_join.tail())

# 3. Introduce missing values
employees_extended.loc[2, "salary"] = np.nan
employees_extended.loc[8, "years_experience"] = np.nan

print("\nMissing values count:")
print(employees_extended.isna().sum())

# 4. Fill with mean
employees_clean = employees_extended.copy()

employees_clean["salary"] = (
    employees_clean["salary"]
    .fillna(employees_clean["salary"].mean())
)

employees_clean["years_experience"] = (
    employees_clean["years_experience"]
    .fillna(employees_clean["years_experience"].mean())
)

print("\nAfter filling missing values:")
print(employees_clean.isna().sum())