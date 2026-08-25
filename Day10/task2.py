# Analyse data with Pandas — loading, filtering, grouping, and aggregation
import pandas as pd
data = {
    "name": [
        "Arun", "Bala", "Charan", "David", "Elan",
        "Fahad", "Ganesh", "Hari", "Ishan", "John",
        "Kiran", "Lokesh", "Manoj", "Naveen", "Prakash"
    ],

    "department": [
        "IT", "HR", "IT", "Finance", "HR",
        "IT", "Finance", "IT", "HR", "Finance",
        "IT", "HR", "Finance", "IT", "HR"
    ],

    "salary": [
        50000, 40000, 60000, 55000, 45000,
        70000, 65000, 52000, 48000, 58000,
        75000, 42000, 62000, 68000, 46000
    ],

    "years_experience": [
        2, 3, 4, 5, 3,
        6, 5, 4, 2, 4,
        7, 3, 6, 5, 2
    ]
}

df = pd.DataFrame(data)
df.to_csv("Day10/employees.csv", index=False)
print("CSV file created.")
df = pd.read_csv("Day10/employees.csv")
print("\nEmployee Data:")
print(df)

print("\nDataFrame Information:")
df.info()
print("\nDataFrame Description:")
print(df.describe())

it_employees = df[df["department"] == "IT"]
print("\nIT employees using boolean indexing:")
print(it_employees)

it_employees_query = df.query("department == 'IT'")
print("\nIT employees using query():")
print(it_employees_query)

summary = df.groupby("department").agg(
    average_salary=("salary", "mean"),
    headcount=("name", "count")
)

print("\nDepartment Summary:")
print(summary)

summary = summary.sort_values(
    "average_salary",
    ascending=False
)

print("\nSorted Department Summary:")
print(summary)



# Output:
# CSV file created.

# Employee Data:
#        name department  salary  years_experience
# 0      Arun         IT   50000                 2
# 1      Bala         HR   40000                 3
# 2    Charan         IT   60000                 4
# 3     David    Finance   55000                 5
# 4      Elan         HR   45000                 3
# 5     Fahad         IT   70000                 6
# 6    Ganesh    Finance   65000                 5
# 7      Hari         IT   52000                 4
# 8     Ishan         HR   48000                 2
# 9      John    Finance   58000                 4
# 10    Kiran         IT   75000                 7
# 11   Lokesh         HR   42000                 3
# 12    Manoj    Finance   62000                 6
# 13   Naveen         IT   68000                 5
# 14  Prakash         HR   46000                 2

# DataFrame Information:
# <class 'pandas.DataFrame'>
# RangeIndex: 15 entries, 0 to 14
# Data columns (total 4 columns):
#  #   Column            Non-Null Count  Dtype
# ---  ------            --------------  -----
#  0   name              15 non-null     str  
#  1   department        15 non-null     str  
#  2   salary            15 non-null     int64
#  3   years_experience  15 non-null     int64
# dtypes: int64(2), str(2)
# memory usage: 612.0 bytes

# DataFrame Description:
#              salary  years_experience
# count     15.000000         15.000000
# mean   55733.333333          4.066667
# std    10780.052125          1.579632
# min    40000.000000          2.000000
# 25%    47000.000000          3.000000
# 50%    55000.000000          4.000000
# 75%    63500.000000          5.000000
# max    75000.000000          7.000000

# IT employees using boolean indexing:
#       name department  salary  years_experience
# 0     Arun         IT   50000                 2
# 2   Charan         IT   60000                 4
# 5    Fahad         IT   70000                 6
# 7     Hari         IT   52000                 4
# 10   Kiran         IT   75000                 7
# 13  Naveen         IT   68000                 5

# IT employees using query():
#       name department  salary  years_experience
# 0     Arun         IT   50000                 2
# 2   Charan         IT   60000                 4
# 5    Fahad         IT   70000                 6
# 7     Hari         IT   52000                 4
# 10   Kiran         IT   75000                 7
# 13  Naveen         IT   68000                 5

# Department Summary:
#             average_salary  headcount
# department                           
# Finance            60000.0          4
# HR                 44200.0          5
# IT                 62500.0          6

# Sorted Department Summary:
#             average_salary  headcount
# department                           
# IT                 62500.0          6
# Finance            60000.0          4
# HR                 44200.0          5