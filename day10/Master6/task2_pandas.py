import pandas as pd

employees_data = {
    "name": ["Amit", "Neha", "Ravi", "Priya", "Karan", "Anjali", "Rahul", "Sneha",
             "Vikram", "Pooja", "Arjun", "Meera", "Rohit", "Kavya", "Sanjay"],
    "department": ["IT", "HR", "Sales", "IT", "Finance", "HR", "Sales", "IT",
                   "Finance", "HR", "Sales", "IT", "Finance", "HR", "Sales"],
    "salary": [65000, 48000, 55000, 72000, 68000, 52000, 60000, 75000,
               70000, 50000, 58000, 80000, 73000, 54000, 62000],
    "years_experience": [3, 2, 4, 5, 6, 3, 5, 7, 8, 2, 4, 9, 7, 3, 6]
}

employees = pd.DataFrame(employees_data)
employees.to_csv("employees.csv", index=False)

df = pd.read_csv("employees.csv")

print("DataFrame information:")
df.info()
print("\nDataFrame description:")
print(df.describe())

it_boolean = df[df["department"] == "IT"]
it_query = df.query("department == 'IT'")

print("\nIT employees using boolean indexing:")
print(it_boolean)
print("\nIT employees using query:")
print(it_query)
print("\nBoth filters are same:", it_boolean.equals(it_query))

department_summary = df.groupby("department").agg(
    average_salary=("salary", "mean"),
    headcount=("name", "count")
).sort_values("average_salary", ascending=False)

print("\nDepartment summary:")
print(department_summary)


# OUTPUT

# DataFrame information:
# <class 'pandas.core.frame.DataFrame'>
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
#
# DataFrame description:
#              salary  years_experience
# count     15.000000         15.000000
# mean   62800.000000          4.933333
# std     9951.310036          2.186539
# min    48000.000000          2.000000
# 25%    54500.000000          3.000000
# 50%    62000.000000          5.000000
# 75%    71000.000000          6.500000
# max    80000.000000          9.000000
#
# IT employees using boolean indexing:
#      name department  salary  years_experience
# 0    Amit         IT   65000                 3
# 3   Priya         IT   72000                 5
# 7   Sneha         IT   75000                 7
# 11  Meera         IT   80000                 9
#
# IT employees using query:
#      name department  salary  years_experience
# 0    Amit         IT   65000                 3
# 3   Priya         IT   72000                 5
# 7   Sneha         IT   75000                 7
# 11  Meera         IT   80000                 9
# Both filters are same: True
# Department summary:
#             average_salary  headcount
# department
# IT            73000.000000          4
# Finance       70333.333333          3
# Sales         58750.000000          4
# HR            51000.000000          4
