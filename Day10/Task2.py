import pandas as pd
 
employees = pd.DataFrame({
    "name": [
        "Alice", "Bob", "Charlie", "David", "Emma",
        "Frank", "Grace", "Henry", "Ivy", "Jack",
        "Kelly", "Liam", "Mason", "Nina", "Olivia"
    ],
    "department": [
        "IT", "HR", "Finance", "IT", "HR",
        "Finance", "IT", "HR", "Finance", "IT",
        "HR", "Finance", "IT", "HR", "Finance"
    ],
    "salary": [
        70000, 50000, 80000, 75000, 52000,
        85000, 72000, 55000, 83000, 78000,
        56000, 87000, 79000, 58000, 90000
    ],
    "years_experience": [
        5, 3, 8, 6, 4,
        10, 5, 2, 9, 7,
        3, 11, 8, 4, 12
    ]
})
 
employees.to_csv("employees.csv", index=False)
 
df = pd.read_csv("employees.csv")
 
print(df.info())
print(df.describe())
 
# 2. Filter using boolean indexing
it_boolean = df[df["department"] == "IT"]
 
# Filter using query
it_query = df.query("department == 'IT'")
 
print("\nBoolean Filter:")
print(it_boolean)
 
print("\nQuery Filter:")
print(it_query)
 
print("\nSame rows:", it_boolean.equals(it_query))
 
# 3. Groupby aggregation
grouped = (
    df.groupby("department")
      .agg(
          avg_salary=("salary", "mean"),
          headcount=("name", "count")
      )
)
 
# 4. Sort descending
grouped_sorted = grouped.sort_values(
    by="avg_salary",
    ascending=False
)
 
print("\nGrouped Summary:")
print(grouped_sorted)
 
# Output
"""
<class 'pandas.DataFrame'>
RangeIndex: 15 entries, 0 to 14
Data columns (total 4 columns):
 #   Column            Non-Null Count  Dtype
---  ------            --------------  -----
 0   name              15 non-null     str  
 1   department        15 non-null     str  
 2   salary            15 non-null     int64
 3   years_experience  15 non-null     int64
dtypes: int64(2), str(2)
memory usage: 612.0 bytes
None
             salary  years_experience
count     15.000000         15.000000
mean   71333.333333          6.466667
std    13678.276138          3.113718
min    50000.000000          2.000000
25%    57000.000000          4.000000
50%    75000.000000          6.000000
75%    81500.000000          8.500000
max    90000.000000         12.000000
 
Boolean Filter:
     name department  salary  years_experience
0   Alice         IT   70000                 5
3   David         IT   75000                 6
6   Grace         IT   72000                 5
9    Jack         IT   78000                 7
12  Mason         IT   79000                 8
 
Query Filter:
     name department  salary  years_experience
0   Alice         IT   70000                 5
3   David         IT   75000                 6
6   Grace         IT   72000                 5
9    Jack         IT   78000                 7
12  Mason         IT   79000                 8
 
Same rows: True
 
Grouped Summary:
            avg_salary  headcount
department                      
Finance        85000.0          5
IT             74800.0          5
HR             54200.0          5
"""
 