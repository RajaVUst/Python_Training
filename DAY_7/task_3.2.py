import csv
import os

base = os.path.dirname(__file__)
csv_path = os.path.join(base, "employees.csv")
updated_path = os.path.join(base, "employees_updated.csv")

employees = [
    {"name": "Alice",   "department": "Engineering", "salary": 95000},
    {"name": "Bob",     "department": "Marketing",   "salary": 72000},
    {"name": "Carol",   "department": "Engineering", "salary": 105000},
    {"name": "David",   "department": "HR",          "salary": 68000},
    {"name": "Eva",     "department": "Marketing",   "salary": 78000},
]

# Write employees.csv
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "department", "salary"])
    for emp in employees:
        writer.writerow([emp["name"], emp["department"], emp["salary"]])

# Read back with DictReader
print("--- Employee Records ---")
rows = []
with open(csv_path, "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(dict(row))
        rows.append(dict(row))

# Total salary per department
dept_totals = {}
for row in rows:
    dept = row["department"]
    dept_totals[dept] = dept_totals.get(dept, 0) + float(row["salary"])

print("\nTotal salary per department:", dept_totals)

# 10% raise for Engineering, write updated CSV
print("\nApplying 10% raise to Engineering...")
with open(updated_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "department", "salary"])
    writer.writeheader()
    for row in rows:
        if row["department"] == "Engineering":
            row["salary"] = round(float(row["salary"]) * 1.10, 2)
        writer.writerow(row)

print("Written to employees_updated.csv")
