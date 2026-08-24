
#Merge DataFrames and handle missing data sensibly
import pandas as pd
import numpy as np
 
employees = pd.DataFrame({
    "name": [
        "Arun", "Bala", "Charan", "David", "Elan",
        "Fahad", "Ganesh", "Hari", "Ishan", "John"
    ],
 
    "department": [
        "IT", "HR", "IT", "Finance", "HR",
        "IT", "Finance", "IT", "HR", "Sales"
    ],
 
    "salary": [
        50000, 40000, 60000, 55000, 45000,
        70000, 65000, 52000, 48000, 50000
    ],
 
    "years_experience": [
        2, 3, 4, 5, 3,
        6, 5, 4, 2, 3
    ]
})
 
departments = pd.DataFrame({
    "department": [
        "IT",
        "HR",
        "Finance"
    ],
 
    "department_budget": [
        1000000,
        500000,
        800000
    ]
})
 
 
print("Employees:")
print(employees)
 
print("\nDepartments:")
print(departments)
 
 
#inner join
inner_join = pd.merge(
    employees,
    departments,
    on="department",
    how="inner"
)
 
print("\nInner Join:")
print(inner_join)
 
 
#left join
left_join = pd.merge(
    employees,
    departments,
    on="department",
    how="left"
)
 
print("\nLeft Join:")
print(left_join)
 
employees.loc[1, "salary"] = np.nan
employees.loc[4, "years_experience"] = np.nan
print("\nEmployees with missing values:")
print(employees)
print("\nNumber of missing values:")
print(employees.isna().sum())
 
average_salary = employees["salary"].mean()
employees["salary"] = employees["salary"].fillna(average_salary)
print("\nAfter handling missing salary:")
print(employees)
 
 
# Output:
# Employees:
#      name department  salary  years_experience
# 0    Arun         IT   50000                 2
# 1    Bala         HR   40000                 3
# 2  Charan         IT   60000                 4
# 3   David    Finance   55000                 5
# 4    Elan         HR   45000                 3
# 5   Fahad         IT   70000                 6
# 6  Ganesh    Finance   65000                 5
# 7    Hari         IT   52000                 4
# 8   Ishan         HR   48000                 2
# 9    John      Sales   50000                 3
 
# Departments:
#   department  department_budget
# 0         IT            1000000
# 1         HR             500000
# 2    Finance             800000
 
# Inner Join:
#      name department  salary  years_experience  department_budget
# 0    Arun         IT   50000                 2            1000000
# 1    Bala         HR   40000                 3             500000
# 2  Charan         IT   60000                 4            1000000
# 3   David    Finance   55000                 5             800000
# 4    Elan         HR   45000                 3             500000
# 5   Fahad         IT   70000                 6            1000000
# 6  Ganesh    Finance   65000                 5             800000
# 7    Hari         IT   52000                 4            1000000
# 8   Ishan         HR   48000                 2             500000
 
# Left Join:
#      name department  salary  years_experience  department_budget
# 0    Arun         IT   50000                 2          1000000.0
# 1    Bala         HR   40000                 3           500000.0
# 2  Charan         IT   60000                 4          1000000.0
# 3   David    Finance   55000                 5           800000.0
# 4    Elan         HR   45000                 3           500000.0
# 5   Fahad         IT   70000                 6          1000000.0
# 6  Ganesh    Finance   65000                 5           800000.0
# 7    Hari         IT   52000                 4          1000000.0
# 8   Ishan         HR   48000                 2           500000.0
# 9    John      Sales   50000                 3                NaN
 
# Employees with missing values:
#      name department   salary  years_experience
# 0    Arun         IT  50000.0               2.0
# 1    Bala         HR      NaN               3.0
# 2  Charan         IT  60000.0               4.0
# 3   David    Finance  55000.0               5.0
# 4    Elan         HR  45000.0               NaN
# 5   Fahad         IT  70000.0               6.0
# 6  Ganesh    Finance  65000.0               5.0
# 7    Hari         IT  52000.0               4.0
# 8   Ishan         HR  48000.0               2.0
# 9    John      Sales  50000.0               3.0
 
# Number of missing values:
# name                0
# department          0
# salary              1
# years_experience    1
# dtype: int64
 
# After handling missing salary:
#      name department   salary  years_experience
# 0    Arun         IT  50000.0               2.0
# 1    Bala         HR  55000.0               3.0
# 2  Charan         IT  60000.0               4.0
# 3   David    Finance  55000.0               5.0
# 4    Elan         HR  45000.0               NaN
# 5   Fahad         IT  70000.0               6.0
# 6  Ganesh    Finance  65000.0               5.0
# 7    Hari         IT  52000.0               4.0
# 8   Ishan         HR  48000.0               2.0
# 9    John      Sales  50000.0               3.0