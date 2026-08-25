# Task 3 - Join the Data
# Merge DataFrames (inner + left join) and handle missing data

import pandas as pd
import numpy as np

# Reuse employees data from Task 2
employees = pd.read_csv("employees.csv")

# ─── Create departments DataFrame ─────────────────────────────────────────────
departments = pd.DataFrame({
    "department":        ["Engineering", "Marketing", "HR"],
    "department_budget": [500000, 200000, 150000]
})

# ─── 1. Inner join — only employees whose dept exists in departments ───────────
inner = pd.merge(employees, departments, on="department", how="inner")
print("=== Inner Join ===")
print(inner[["name", "department", "department_budget"]].head())

# ─── 2. Left join — add an employee with an unknown department ────────────────
new_employee = pd.DataFrame([{
    "name": "Zara", "department": "Legal", "salary": 90000, "years_experience": 4
}])
employees_extended = pd.concat([employees, new_employee], ignore_index=True)

left = pd.merge(employees_extended, departments, on="department", how="left")
print("\n=== Left Join (Zara has NaN budget — Legal not in departments) ===")
print(left[left["name"] == "Zara"])   # NaN in department_budget

# ─── 3. Introduce missing values and detect them ─────────────────────────────
employees.loc[2, "salary"] = np.nan
employees.loc[7, "years_experience"] = np.nan

print("\n=== Missing value counts ===")
print(employees.isna().sum())

# ─── 4. Handle missing values — fill salary with column mean ─────────────────
# Filling with the mean keeps all rows and is statistically reasonable for salary.
# Dropping rows would lose valid data from other columns.
mean_salary = employees["salary"].mean()
employees["salary"] = employees["salary"].fillna(mean_salary)

mean_exp = employees["years_experience"].mean()
employees["years_experience"] = employees["years_experience"].fillna(mean_exp)

print("\n=== After filling NaNs ===")
print(employees.isna().sum())
print(employees[["name", "salary", "years_experience"]].to_string())
