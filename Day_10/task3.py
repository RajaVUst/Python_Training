import pandas as pd
import numpy as np

employees = pd.DataFrame({
    "name": ["John", "Alice", "Bob", "David", "Emma", "Unknown"],
    "department": ["IT", "HR", "IT", "Finance", "HR", "Legal"],
    "salary": [60000, 50000, np.nan, 70000, np.nan, 55000],
    "years_experience": [3, 2, 4, 6, 5, 2]
})

departments = pd.DataFrame({
    "department": ["IT", "HR", "Finance"],
    "department_budget": [500000, 300000, 700000]
})

inner_join = pd.merge(
    employees,
    departments,
    on="department",
    how="inner",
    validate="many_to_one"
)

left_join = pd.merge(
    employees,
    departments,
    on="department",
    how="left",
    validate="many_to_one"
)

print(inner_join)
print(left_join)

print(employees.isna().sum())

employees["salary"] = employees["salary"].fillna(
    employees["salary"].mean()
)

print(employees)

# Filled salary NaN values with mean salary because salary is
# numeric data and mean imputation preserves overall trends.

# Output:
# Inner join excludes Legal department employee
# Left join shows NaN budget for Legal department
# Missing value counts displayed
# Updated DataFrame with filled salaries displayed