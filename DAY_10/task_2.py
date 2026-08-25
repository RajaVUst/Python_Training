# Task 2 - Load & Explore
# Pandas: create CSV, read it, filter, groupby, aggregate, sort

import pandas as pd
import io

# ─── Create the CSV data in code ──────────────────────────────────────────────
csv_data = """name,department,salary,years_experience
Alice,Engineering,95000,5
Bob,Engineering,85000,3
Carol,Engineering,110000,8
Dave,Marketing,60000,2
Eve,Marketing,70000,4
Frank,Marketing,65000,3
Grace,HR,55000,6
Henry,HR,50000,1
Ivy,HR,58000,4
Jack,Engineering,120000,10
Kate,Marketing,75000,6
Leo,HR,52000,2
Mia,Engineering,98000,6
Nina,Marketing,68000,3
Oscar,Engineering,105000,7
"""

# Save to a CSV file, then read it back
with open("employees.csv", "w") as f:
    f.write(csv_data)

df = pd.read_csv("employees.csv")

# ─── 1. Explore the data ──────────────────────────────────────────────────────
print("=== df.info() ===")
df.info()
print("\n=== df.describe() ===")
print(df.describe())

# ─── 2. Filter to a single department — two ways ─────────────────────────────
# Boolean indexing
bool_filter = df[df["department"] == "Engineering"]
print("\n--- Engineering (boolean indexing) ---")
print(bool_filter[["name", "salary"]])

# .query() — same result
query_filter = df.query("department == 'Engineering'")
print("\n--- Engineering (.query()) ---")
print(query_filter[["name", "salary"]])

# Confirm they match
print("Both filters match:", bool_filter.equals(query_filter))

# ─── 3. Group by department, compute avg salary and headcount ─────────────────
summary = df.groupby("department")["salary"].agg(
    avg_salary="mean",
    headcount="count"
)

# ─── 4. Sort by avg salary descending ────────────────────────────────────────
summary = summary.sort_values("avg_salary", ascending=False)
print("\n=== Department Summary (sorted by avg salary) ===")
print(summary.round(0))
