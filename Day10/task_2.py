import pandas as pd

# Create employee data
employees = {
    "name": [
        "Alice", "Bob", "Carol", "David", "Eve",
        "Frank", "Grace", "Henry", "Ivy", "Jack",
        "Kate", "Leo", "Mia", "Noah", "Olivia"
    ],
    "department": [
        "Engineering", "HR", "Engineering", "Sales", "HR",
        "Engineering", "Sales", "Engineering", "HR", "Sales",
        "Engineering", "HR", "Sales", "Engineering", "Sales"
    ],
    "salary": [
        75000, 55000, 82000, 60000, 58000,
        90000, 65000, 85000, 62000, 70000,
        95000, 59000, 68000, 88000, 72000
    ],
    "years_experience": [
        3, 2, 5, 4, 3,
        7, 5, 6, 4, 6,
        8, 3, 5, 7, 6
    ]
}

# Create DataFrame
df = pd.DataFrame(employees)

# Save data to CSV
df.to_csv("employees.csv", index=False)

# Read CSV
df = pd.read_csv("employees.csv")

#  Display information about the DataFrame
print("DataFrame Info:")
print(df.info())

print("\nDataFrame Description:")
print(df.describe())

#  Filter Engineering employees using boolean indexing
engineering_1 = df[df["department"] == "Engineering"]

print("\nEngineering employees - Boolean indexing:")
print(engineering_1)

# Filter Engineering employees using query()
engineering_2 = df.query("department == 'Engineering'")

print("\nEngineering employees - query():")
print(engineering_2)

# Check whether both filtering methods return the same rows
print("\nBoth filtering methods give the same result:",
      engineering_1.equals(engineering_2))

#  Group by department and calculate average salary and headcount
summary = df.groupby("department").agg(
    average_salary=("salary", "mean"),
    headcount=("name", "count")
)

#  Sort by average salary in descending order
summary = summary.sort_values("average_salary", ascending=False)

print("\nDepartment Summary:")
print(summary)





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
# None

# DataFrame Description:
#              salary  years_experience
# count     15.000000         15.000000
# mean   72266.666667          4.933333
# std    12964.052864          1.751190
# min    55000.000000          2.000000
# 25%    61000.000000          3.500000
# 50%    70000.000000          5.000000
# 75%    83500.000000          6.000000
# max    95000.000000          8.000000

# Engineering employees - Boolean indexing:
#      name   department  salary  years_experience
# 0   Alice  Engineering   75000                 3
# 2   Carol  Engineering   82000                 5
# 5   Frank  Engineering   90000                 7
# 7   Henry  Engineering   85000                 6
# 10   Kate  Engineering   95000                 8
# 13   Noah  Engineering   88000                 7

# Engineering employees - query():
#      name   department  salary  years_experience
# 0   Alice  Engineering   75000                 3
# 2   Carol  Engineering   82000                 5
# 5   Frank  Engineering   90000                 7
# 7   Henry  Engineering   85000                 6
# 10   Kate  Engineering   95000                 8
# 13   Noah  Engineering   88000                 7

# Both filtering methods give the same result: True

# Department Summary:
#              average_salary  headcount
# department                            
# Engineering    85833.333333          6
# Sales          67000.000000          5
# HR             58500.000000          4
