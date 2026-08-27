import numpy as np
import pandas as pd

employees = pd.read_csv("employees.csv")

new_employee = pd.DataFrame({
    "name": ["Nitin"],
    "department": ["Legal"],
    "salary": [67000],
    "years_experience": [5]
})
employees = pd.concat([employees, new_employee], ignore_index=True)

departments = pd.DataFrame({
    "department": ["IT", "HR", "Sales", "Finance"],
    "department_budget": [1000000, 500000, 800000, 900000]
})

inner_result = pd.merge(employees, departments, on="department", how="inner")
left_result = pd.merge(employees, departments, on="department", how="left")

print("Employees in inner join:", len(inner_result))
print("Employees in left join:", len(left_result))
print("\nLegal employee after left join:")
print(left_result[left_result["department"] == "Legal"])

employees.loc[1, "salary"] = np.nan
employees.loc[6, "years_experience"] = np.nan

print("\nMissing values before filling:")
print(employees.isna().sum())

employees["salary"] = employees["salary"].fillna(employees["salary"].mean())
employees["years_experience"] = employees["years_experience"].fillna(
    employees["years_experience"].mean()
)

print("\nMissing values after filling:")
print(employees.isna().sum())


# OUTPUT

# Employees in inner join: 15
# Employees in left join: 16
#
# Legal employee after left join:
#      name department  salary  years_experience  department_budget
# 15  Nitin      Legal   67000                 5                NaN
#
# Missing values before filling:
# name                0
# department          0
# salary              1
# years_experience    1
# dtype: int64
#
# Missing values after filling:
# name                0
# department          0
# salary              0
# years_experience    0
# dtype: int64
