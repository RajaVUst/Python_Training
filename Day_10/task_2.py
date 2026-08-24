#task2
import pandas as pd
 
employees = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva",
             "Frank", "Grace", "Henry", "Isabella", "Jack",
             "Karen", "Leo", "Mia", "Noah", "Olivia"],
    "department": ["IT", "HR", "IT", "Finance", "HR",
                   "Finance", "IT", "Marketing", "Marketing", "HR",
                   "Finance", "IT", "Marketing", "Finance", "HR"],
    "salary": [70000, 50000, 75000, 65000, 52000,
               68000, 72000, 58000, 60000, 54000,
               70000, 78000, 62000, 72000, 56000],
    "years_experience": [5, 3, 6, 4, 2,
                         5, 7, 3, 4, 2,
                         6, 8, 5, 7, 3]
}
df = pd.DataFrame(employees)
df.to_csv("employees.csv", index=False)
df = pd.read_csv("employees.csv")
 
# PART 1: DATA EXPLORATION
print("PART 1 OUTPUT")
print("\nDataFrame Info:")
df.info()
print("\nDataFrame Description:")
print(df.describe())
print()
'''
PART 1 OUTPUT
 
DataFrame Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 15 entries, 0 to 14
Data columns (total 4 columns):
 #   Column             Non-Null Count  Dtype
---  ------             --------------  -----
 0   name               15 non-null     object
 1   department         15 non-null     object
 2   salary             15 non-null     int64
 3   years_experience   15 non-null     int64
dtypes: int64(2), object(2)
memory usage: 612.0+ bytes
 
DataFrame Description:
              salary  years_experience
count      15.000000         15.000000
mean    63466.666667          4.666667
std      9890.879518          1.877181
min     50000.000000          2.000000
25%     57000.000000          3.000000
50%     65000.000000          5.000000
75%     71000.000000          6.500000
max     78000.000000          8.000000
'''
 
df = pd.read_csv("employees.csv")
it_boolean = df[df["department"] == "IT"]
print("PART 2 OUTPUT")
print("\nIT Department (Boolean Indexing):")
print(it_boolean)
it_query = df.query("department == 'IT'")
print("\nIT Department (.query()):")
print(it_query)
print("\nResults identical:")
print(it_boolean.equals(it_query))
summary = (
    df.groupby("department")
      .agg(
          average_salary=("salary", "mean"),
          headcount=("name", "count")
      )
      .sort_values(by="average_salary", ascending=False)
)
print("\nGrouped Summary:")
print(summary)
'''
PART 2 OUTPUT
 
IT Department (Boolean Indexing):
       name department  salary  years_experience
0     Alice         IT   70000                 5
2   Charlie         IT   75000                 6
6     Grace         IT   72000                 7
11      Leo         IT   78000                 8
 
IT Department (.query()):
       name department  salary  years_experience
0     Alice         IT   70000                 5
2   Charlie         IT   75000                 6
6     Grace         IT   72000                 7
11      Leo         IT   78000                 8
 
Results identical:
True
 
Grouped Summary:
            average_salary  headcount
department
IT                73750.0          4
Finance           68750.0          4
Marketing         60000.0          3
HR                53000.0          4
'''
 
#note
'''
Pandas makes it easy to load and analyze structured data
using DataFrames.
 
df.info() provides information about columns, data types,
and missing values, while df.describe() generates summary
statistics for numeric columns.
 
Boolean indexing filters rows by applying a condition
directly on a column.
 
The .query() method provides an alternative SQL-like syntax
for filtering DataFrame rows.
 
Both boolean indexing and .query() return the same rows,
which is verified using the equals() method.
 
The groupby() operation groups employees by department,
while .agg() computes multiple aggregate statistics in a
single operation.
 
The grouped summary calculates the average salary and
employee headcount for each department.
 
sort_values(..., ascending=False) sorts departments from
highest average salary to lowest average salary, satisfying
the acceptance criteria.
'''