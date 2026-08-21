
import csv


employees = [
    ["Alice", "Engineering", 70000],
    ["Bob", "HR", 50000],
    ["Carol", "Engineering", 80000],
    ["David", "Sales", 60000],
    ["Emma", "HR", 55000]
]
with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "department", "salary"])
    writer.writerows(employees)
department_totals = {}
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        dept = row["department"]
        salary = float(row["salary"])
        department_totals[dept] = department_totals.get(dept, 0) + salary
print("\nDepartment Salary Totals:")
print(department_totals)
updated_rows = []
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["department"] == "Engineering":
            row["salary"] = str(float(row["salary"]) * 1.10)
        updated_rows.append(row)
with open("employees_updated.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["name", "department", "salary"]
    )
    writer.writeheader()
    writer.writerows(updated_rows)
print("\nUpdated file created: employees_updated.csv")
print()
#  Output:
# {'name': 'Alice', 'department': 'Engineering', 'salary': '70000'}
# {'name': 'Bob', 'department': 'HR', 'salary': '50000'}
# {'name': 'Carol', 'department': 'Engineering', 'salary': '80000'}
# {'name': 'David', 'department': 'Sales', 'salary': '60000'}
# {'name': 'Emma', 'department': 'HR', 'salary': '55000'}
# Department Salary Totals:
# {'Engineering': 150000.0, 'HR': 105000.0, 'Sales': 60000.0}
# Updated file created: employees_updated.csv