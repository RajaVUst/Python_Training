# Day 10 - Task 3
# from http.cookiejar import unmatched

import numpy as np
import pandas as pd

from Day10.Task2 import employees

# Department information
departments = pd.DataFrame({
    "department": [
        "Engineering",
        "HR",
        "Sales",
        "Finance"
    ],

    "department_budget": [
        900000,
        250000,
        600000,
        500000
    ]
})

print("Departments:")
print(departments)

# 1. Inner join
inner_join = employees.merge(
    departments,
    on="department",
    how="inner"
)

print("\nInner join:")
print(inner_join)

# 2. Left join

left_join = employees.merge(
    departments,
    on="department",
    how="left"
)

print("\nLeft join:")
print(left_join)


# //showing the unmatched employees
unmatched_employee = left_join[
    left_join["department_budget"].isna()
]

print("\nEmployee with unmatched department:")
print(unmatched_employee)


#introducing missing values

employees_missing = employees.copy()

# 3. Add missing values
employees_missing.loc[2, "salary"] = np.nan
employees_missing.loc[7, "years_experience"] = np.nan

print("\nEmployees with missing values:")
print(employees_missing)


# Count missing values in every column
print("\nMissing-value counts:")
print(employees_missing.isna().sum())




# filling the missing values
# I use the mean because salary and experience are numeric columns,
# and filling allows us to keep every employee in the analysis.

employees_clean = employees_missing.copy()

employees_clean["salary"] = employees_clean["salary"].fillna(
    employees_clean["salary"].mean()
)

employees_clean["years_experience"] = (
    employees_clean["years_experience"].fillna(
        employees_clean["years_experience"].mean()
    )
)

print("\nCleaned employee data:")
print(employees_clean)


print("\nMissing values after cleaning:")
print(employees_clean.isna().sum())


#output

'''
CSV file created successfully.
Employee DataFrame:
           name   department  salary  years_experience
0           Sai  Engineering   85000                 3
1           ram           HR   52000                 2
2       Krishna        Sales   61000                 4
3        athira  Engineering   92000                 6
4     aishwarya      Finance   73000                 5
5        Ananya        Sales   65000                 3
6        Vikram  Engineering  105000                 8
7          Isha           HR   56000                 4
8         Arjun      Finance   78000                 6
9         Nisha        Sales   68000                 5
10        Rahul  Engineering   88000                 4
11        Priya      Finance   81000                 7
12        Kiran           HR   59000                 5
13        Sneha        Sales   72000                 6
14         Deva  Engineering   98000                 7
15  Devika Tara        Legal   70000                 3

DataFrame information:
<class 'pandas.DataFrame'>
RangeIndex: 16 entries, 0 to 15
Data columns (total 4 columns):
 #   Column            Non-Null Count  Dtype
---  ------            --------------  -----
 0   name              16 non-null     str  
 1   department        16 non-null     str  
 2   salary            16 non-null     int64
 3   years_experience  16 non-null     int64
dtypes: int64(2), str(2)
memory usage: 644.0 bytes

Statistical summary:
              salary  years_experience
count      16.000000         16.000000
mean    75187.500000          4.875000
std     15406.573272          1.707825
min     52000.000000          2.000000
25%     64000.000000          3.750000
50%     72500.000000          5.000000
75%     85750.000000          6.000000
max    105000.000000          8.000000

Engineering employees using boolean indexing:
      name   department  salary  years_experience
0      Sai  Engineering   85000                 3
3   athira  Engineering   92000                 6
6   Vikram  Engineering  105000                 8
10   Rahul  Engineering   88000                 4
14    Deva  Engineering   98000                 7

Engineering employees using query:
      name   department  salary  years_experience
0      Sai  Engineering   85000                 3
3   athira  Engineering   92000                 6
6   Vikram  Engineering  105000                 8
10   Rahul  Engineering   88000                 4
14    Deva  Engineering   98000                 7

Are both filtering results identical? True

Department summary:
             average_salary  headcount
department                            
Engineering    93600.000000          5
Finance        77333.333333          3
HR             55666.666667          3
Legal          70000.000000          1
Sales          66500.000000          4

Departments sorted by average salary:
             average_salary  headcount
department                            
Engineering    93600.000000          5
Finance        77333.333333          3
Legal          70000.000000          1
Sales          66500.000000          4
HR             55666.666667          3
Departments:
    department  department_budget
0  Engineering             900000
1           HR             250000
2        Sales             600000
3      Finance             500000

Inner join:
         name   department  salary  years_experience  department_budget
0         Sai  Engineering   85000                 3             900000
1         ram           HR   52000                 2             250000
2     Krishna        Sales   61000                 4             600000
3      athira  Engineering   92000                 6             900000
4   aishwarya      Finance   73000                 5             500000
5      Ananya        Sales   65000                 3             600000
6      Vikram  Engineering  105000                 8             900000
7        Isha           HR   56000                 4             250000
8       Arjun      Finance   78000                 6             500000
9       Nisha        Sales   68000                 5             600000
10      Rahul  Engineering   88000                 4             900000
11      Priya      Finance   81000                 7             500000
12      Kiran           HR   59000                 5             250000
13      Sneha        Sales   72000                 6             600000
14       Deva  Engineering   98000                 7             900000

Left join:
           name   department  salary  years_experience  department_budget
0           Sai  Engineering   85000                 3           900000.0
1           ram           HR   52000                 2           250000.0
2       Krishna        Sales   61000                 4           600000.0
3        athira  Engineering   92000                 6           900000.0
4     aishwarya      Finance   73000                 5           500000.0
5        Ananya        Sales   65000                 3           600000.0
6        Vikram  Engineering  105000                 8           900000.0
7          Isha           HR   56000                 4           250000.0
8         Arjun      Finance   78000                 6           500000.0
9         Nisha        Sales   68000                 5           600000.0
10        Rahul  Engineering   88000                 4           900000.0
11        Priya      Finance   81000                 7           500000.0
12        Kiran           HR   59000                 5           250000.0
13        Sneha        Sales   72000                 6           600000.0
14         Deva  Engineering   98000                 7           900000.0
15  Devika Tara        Legal   70000                 3                NaN

Employee with unmatched department:
           name department  salary  years_experience  department_budget
15  Devika Tara      Legal   70000                 3                NaN

Employees with missing values:
           name   department    salary  years_experience
0           Sai  Engineering   85000.0               3.0
1           ram           HR   52000.0               2.0
2       Krishna        Sales       NaN               4.0
3        athira  Engineering   92000.0               6.0
4     aishwarya      Finance   73000.0               5.0
5        Ananya        Sales   65000.0               3.0
6        Vikram  Engineering  105000.0               8.0
7          Isha           HR   56000.0               NaN
8         Arjun      Finance   78000.0               6.0
9         Nisha        Sales   68000.0               5.0
10        Rahul  Engineering   88000.0               4.0
11        Priya      Finance   81000.0               7.0
12        Kiran           HR   59000.0               5.0
13        Sneha        Sales   72000.0               6.0
14         Deva  Engineering   98000.0               7.0
15  Devika Tara        Legal   70000.0               3.0

Missing-value counts:
name                0
department          0
salary              1
years_experience    1
dtype: int64

Cleaned employee data:
           name   department         salary  years_experience
0           Sai  Engineering   85000.000000          3.000000
1           ram           HR   52000.000000          2.000000
2       Krishna        Sales   76133.333333          4.000000
3        athira  Engineering   92000.000000          6.000000
4     aishwarya      Finance   73000.000000          5.000000
5        Ananya        Sales   65000.000000          3.000000
6        Vikram  Engineering  105000.000000          8.000000
7          Isha           HR   56000.000000          4.933333
8         Arjun      Finance   78000.000000          6.000000
9         Nisha        Sales   68000.000000          5.000000
10        Rahul  Engineering   88000.000000          4.000000
11        Priya      Finance   81000.000000          7.000000
12        Kiran           HR   59000.000000          5.000000
13        Sneha        Sales   72000.000000          6.000000
14         Deva  Engineering   98000.000000          7.000000
15  Devika Tara        Legal   70000.000000          3.000000

Missing values after cleaning:
name                0
department          0
salary              0
years_experience    0
dtype: int64

Process finished with exit code 0


'''