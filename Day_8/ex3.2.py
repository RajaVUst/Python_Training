import csv

employees = [
    ["Alice", "Engineering", 80000],
    ["Bob", "HR", 60000],
    ["Carol", "Engineering", 90000],
    ["David", "Sales", 70000],
    ["Eva", "HR", 65000]
]

with open(r"Day_8/refdoc/employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "department", "salary"])
    writer.writerows(employees)


with open(r"Day_8/refdoc/employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)

department_totals = {}

with open(r"Day_8/refdoc/employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        dept = row["department"]
        salary = float(row["salary"])
        department_totals[dept] = (
            department_totals.get(dept, 0) + salary
        )

print(department_totals)

updated_rows = []

with open(r"Day_8/refdoc/employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        salary = float(row["salary"])

        if row["department"] == "Engineering":
            salary *= 1.10

        row["salary"] = round(salary, 2)
        updated_rows.append(row)

with open(r"Day_8/refdoc/employees_updated.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["name", "department", "salary"]
    )

    writer.writeheader()
    writer.writerows(updated_rows)

# Output:
"""
{'name': 'Alice', 'department': 'Engineering', 'salary': '80000'}
{'name': 'Bob', 'department': 'HR', 'salary': '60000'}
{'name': 'Carol', 'department': 'Engineering', 'salary': '90000'}
{'name': 'David', 'department': 'Sales', 'salary': '70000'}
{'name': 'Eva', 'department': 'HR', 'salary': '65000'}
{'Engineering': 170000.0, 'HR': 125000.0, 'Sales': 70000.0}
"""