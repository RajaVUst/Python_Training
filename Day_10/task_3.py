import pandas as pd
import numpy as np

# --------------------------------------------------
# Employees DataFrame (from Task 2)
# --------------------------------------------------
employees = pd.DataFrame({
    "name": [
        "Alice", "Bob", "Charlie", "David", "Emma",
        "Frank", "Grace", "Henry", "Ivy", "Jack",
        "Karen", "Leo", "Maria", "Nathan", "Olivia"
    ],
    "department": [
        "IT", "HR", "Finance", "IT", "HR",
        "Finance", "IT", "Sales", "Sales", "HR",
        "Finance", "IT", "Sales", "Finance", "HR"
    ],
    "salary": [
        75000, 55000, 68000, 82000, 60000,
        72000, 78000, 65000, 69000, 58000,
        74000, 85000, 71000, 76000, 62000
    ],
    "years_experience": [
        5, 3, 4, 7, 2,
        6, 5, 4, 3, 2,
        7, 8, 5, 6, 4
    ]
})

# Departments DataFrame
departments = pd.DataFrame({
    "department": ["IT", "HR", "Finance", "Sales"],
    "department_budget": [500000, 250000, 400000, 300000]
})

print("=== Departments DataFrame ===")
print(departments)

# 1. Inner Join
inner_merged = pd.merge(
    employees,
    departments,
    on="department",
    how="inner"
)

print("\n=== Inner Join Result ===")
print(inner_merged)

# 2. Add unmatched employee and perform left join
new_employee = pd.DataFrame({
    "name": ["Sophia"],
    "department": ["Legal"],  # Not in departments table
    "salary": [70000],
    "years_experience": [4]
})

employees_extended = pd.concat(
    [employees, new_employee],
    ignore_index=True
)

left_merged = pd.merge(
    employees_extended,
    departments,
    on="department",
    how="left"
)

print("\n=== Left Join Result ===")
print(left_merged)

# Observe the unmatched row
print("\n=== Rows with Missing Budget ===")
print(left_merged[left_merged["department_budget"].isna()])

# 3. Introduce missing values
employees_extended.loc[2, "salary"] = np.nan
employees_extended.loc[7, "years_experience"] = np.nan

print("\n=== Data with Missing Values ===")
print(employees_extended)

print("\n=== Missing Value Count ===")
print(employees_extended.isna().sum())

# 4. Fill missing values with column means
# Justification:
# Salary and years_experience are numeric columns. Filling
# missing values with the column mean preserves all employee
# records while providing a reasonable estimate for analysis.

employees_cleaned = employees_extended.copy()

employees_cleaned["salary"] = (
    employees_cleaned["salary"]
    .fillna(employees_cleaned["salary"].mean())
)

employees_cleaned["years_experience"] = (
    employees_cleaned["years_experience"]
    .fillna(employees_cleaned["years_experience"].mean())
)

print("\n=== Cleaned Data ===")
print(employees_cleaned)
print("\n=== Missing Values After Cleaning ===")
print(employees_cleaned.isna().sum())