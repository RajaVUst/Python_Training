import pandas as pd
import numpy as np

# Read the employees data created in Task 2
employees = pd.read_csv("employees.csv")

# Create departments DataFrame
departments = pd.DataFrame({
    "department": [
        "Engineering",
        "HR",
        "Sales"
    ],
    "department_budget": [
        500000,
        250000,
        350000
    ]
})

# 1. INNER JOIN

inner_join = pd.merge(
    employees,
    departments,
    on="department",
    how="inner"
)

print("INNER JOIN:")
print(inner_join)


# 2. LEFT JOIN

# Add an employee whose department does not exist
# in the departments table
new_employee = pd.DataFrame({
    "name": ["Peter"],
    "department": ["Marketing"],
    "salary": [65000],
    "years_experience": [4]
})

employees_with_new = pd.concat(
    [employees, new_employee],
    ignore_index=True
)

# Perform LEFT JOIN
left_join = pd.merge(
    employees_with_new,
    departments,
    on="department",
    how="left"
)

print("\nLEFT JOIN:")
print(left_join)


# 3. Introduce missing values

employees_missing = employees.copy()

# Introduce two missing salary values
employees_missing.loc[2, "salary"] = np.nan
employees_missing.loc[7, "salary"] = np.nan

print("\nData with missing values:")
print(employees_missing)

# Detect missing values
print("\nMissing values:")
print(employees_missing.isna().sum())


# 4. Handle missing values

# Salary is a numeric column, so using the mean
# keeps the rows while providing a reasonable estimate
# for the missing salary values.
salary_mean = employees_missing["salary"].mean()

employees_missing["salary"] = employees_missing["salary"].fillna(
    salary_mean
)

print("\nData after filling missing salaries:")
print(employees_missing)

print("\nMissing values after handling:")
print(employees_missing.isna().sum())




# INNER JOIN:
#       name   department  salary  years_experience  department_budget
# 0    Alice  Engineering   75000                 3             500000
# 1      Bob           HR   55000                 2             250000
# 2    Carol  Engineering   82000                 5             500000
# 3    David        Sales   60000                 4             350000
# 4      Eve           HR   58000                 3             250000
# 5    Frank  Engineering   90000                 7             500000
# 6    Grace        Sales   65000                 5             350000
# 7    Henry  Engineering   85000                 6             500000
# 8      Ivy           HR   62000                 4             250000
# 9     Jack        Sales   70000                 6             350000
# 10    Kate  Engineering   95000                 8             500000
# 11     Leo           HR   59000                 3             250000
# 12     Mia        Sales   68000                 5             350000
# 13    Noah  Engineering   88000                 7             500000
# 14  Olivia        Sales   72000                 6             350000

# LEFT JOIN:
#       name   department  salary  years_experience  department_budget
# 0    Alice  Engineering   75000                 3           500000.0
# 1      Bob           HR   55000                 2           250000.0
# 2    Carol  Engineering   82000                 5           500000.0
# 3    David        Sales   60000                 4           350000.0
# 4      Eve           HR   58000                 3           250000.0
# 5    Frank  Engineering   90000                 7           500000.0
# 6    Grace        Sales   65000                 5           350000.0
# 7    Henry  Engineering   85000                 6           500000.0
# 8      Ivy           HR   62000                 4           250000.0
# 9     Jack        Sales   70000                 6           350000.0
# 10    Kate  Engineering   95000                 8           500000.0
# 11     Leo           HR   59000                 3           250000.0
# 12     Mia        Sales   68000                 5           350000.0
# 13    Noah  Engineering   88000                 7           500000.0
# 14  Olivia        Sales   72000                 6           350000.0
# 15   Peter    Marketing   65000                 4                NaN

# Data with missing values:
#       name   department   salary  years_experience
# 0    Alice  Engineering  75000.0                 3
# 1      Bob           HR  55000.0                 2
# 2    Carol  Engineering      NaN                 5
# 3    David        Sales  60000.0                 4
# 4      Eve           HR  58000.0                 3
# 5    Frank  Engineering  90000.0                 7
# 6    Grace        Sales  65000.0                 5
# 7    Henry  Engineering      NaN                 6
# 8      Ivy           HR  62000.0                 4
# 9     Jack        Sales  70000.0                 6
# 10    Kate  Engineering  95000.0                 8
# 11     Leo           HR  59000.0                 3
# 12     Mia        Sales  68000.0                 5
# 13    Noah  Engineering  88000.0                 7
# 14  Olivia        Sales  72000.0                 6

# Missing values:
# name                0
# department          0
# salary              2
# years_experience    0
# dtype: int64

# Data after filling missing salaries:
#       name   department        salary  years_experience
# 0    Alice  Engineering  75000.000000                 3
# 1      Bob           HR  55000.000000                 2
# 2    Carol  Engineering  70538.461538                 5
# 3    David        Sales  60000.000000                 4
# 4      Eve           HR  58000.000000                 3
# 5    Frank  Engineering  90000.000000                 7
# 6    Grace        Sales  65000.000000                 5
# 7    Henry  Engineering  70538.461538                 6
# 8      Ivy           HR  62000.000000                 4
# 9     Jack        Sales  70000.000000                 6
# 10    Kate  Engineering  95000.000000                 8
# 11     Leo           HR  59000.000000                 3
# 12     Mia        Sales  68000.000000                 5
# 13    Noah  Engineering  88000.000000                 7
# 14  Olivia        Sales  72000.000000                 6

# Missing values after handling:
# name                0
# department          0
# salary              0
# years_experience    0
# dtype: int64
