import pandas as pd

# --------------------------------------------------
# Create sample employee data and save as CSV
# --------------------------------------------------
employees = pd.DataFrame({
    "name": [
        "Alice", "Bob", "Charlie", "David", "Emma",
        "Frank", "Grace", "Henry", "Ivy", "Jack",
        "Karen", "Leo", "Maria", "Nathan", "Olivia"
    ],
    "department": [
        "IT", "HR", "Finance", "IT", "HR",
        "Finance", "IT", "Sales", "Sales", "HR",
        "Finance", "IT", "Sales", "Finance", "HR"
    ],
    "salary": [
        75000, 55000, 68000, 82000, 60000,
        72000, 78000, 65000, 69000, 58000,
        74000, 85000, 71000, 76000, 62000
    ],
    "years_experience": [
        5, 3, 4, 7, 2,
        6, 5, 4, 3, 2,
        7, 8, 5, 6, 4
    ]
})

employees.to_csv("employees.csv", index=False)

# --------------------------------------------------
# 1. Read CSV and print info() and describe()
# --------------------------------------------------
df = pd.read_csv("employees.csv")

print("=== DataFrame Info ===")
df.info()

print("\n=== DataFrame Describe ===")
print(df.describe())

# --------------------------------------------------
# 2. Filter a single department
#    Using boolean indexing
# --------------------------------------------------
it_boolean = df[df["department"] == "IT"]

print("\n=== IT Department (Boolean Indexing) ===")
print(it_boolean)

# Using query()
it_query = df.query("department == 'IT'")

print("\n=== IT Department (.query()) ===")
print(it_query)

# Verify both return same rows
print("\nSame rows returned:",
      it_boolean.reset_index(drop=True).equals(
          it_query.reset_index(drop=True)
      ))

# --------------------------------------------------
# 3. Group by department and aggregate
# --------------------------------------------------
summary = (
    df.groupby("department")
      .agg(
          average_salary=("salary", "mean"),
          headcount=("name", "count")
      )
)

print("\n=== Grouped Summary ===")
print(summary)

# --------------------------------------------------
# 4. Sort by average salary descending
# --------------------------------------------------
summary_sorted = summary.sort_values(
    by="average_salary",
    ascending=False
)

print("\n=== Sorted Grouped Summary ===")
print(summary_sorted)