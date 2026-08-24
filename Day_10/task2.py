# Task 2: Data Manipulation with Pandas

import pandas as pd

employees = pd.DataFrame({
    "name": ["John","Alice","Bob","David","Emma","Tom","Sam",
             "Mike","Sara","Chris","Ryan","Sophia","James",
             "Olivia","Daniel"],
    "department": ["IT","HR","IT","Finance","HR","IT","Finance",
                   "IT","HR","Finance","IT","HR","Finance",
                   "IT","Finance"],
    "salary": [60000,50000,65000,70000,52000,62000,72000,
               68000,51000,74000,63000,55000,71000,69000,76000],
    "years_experience": [3,2,4,6,2,5,7,4,3,8,5,4,7,6,9]
})

employees.to_csv("employees.csv", index=False)

df = pd.read_csv("employees.csv")

print(df.info())
print(df.describe())

it1 = df[df["department"] == "IT"]
it2 = df.query("department == 'IT'")

print(it1)
print(it2)

grouped = (
    df.groupby("department")
      .agg(
          average_salary=("salary", "mean"),
          headcount=("name", "count")
      )
      .sort_values("average_salary", ascending=False)
)

print(grouped)

# Output:
# DataFrame info displayed
# Statistical summary displayed
# IT department rows using boolean indexing
# Same IT rows using query()
# Sorted department summary:
#            average_salary  headcount
# Finance           72600.0          5
# IT                64500.0          6
# HR                52000.0          4