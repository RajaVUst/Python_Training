import csv

employees = [
    ["Alice", "Engineering", 70000],
    ["Bob", "Sales", 55000],
    ["Carol", "Engineering", 80000],
    ["Dave", "HR", 50000],
    ["Eve", "Sales", 60000]
]


# Create employees.csv
with open(
    "employees.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)
    writer.writerow(["name", "department", "salary"])
    writer.writerows(employees)


employee_records = []
department_totals = {}


# Read CSV
with open(
    "employees.csv",
    "r",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row)

        salary = float(row["salary"])
        row["salary"] = salary
        employee_records.append(row)

        department = row["department"]

        department_totals[department] = (
            department_totals.get(department, 0) + salary
        )


print("Total salary by department:", department_totals)


# Give Engineering employees a 10% raise
for employee in employee_records:
    if employee["department"] == "Engineering":
        employee["salary"] = round(
            employee["salary"] * 1.10,
            2
        )


# Write updated CSV
with open(
    "employees_updated.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    fieldnames = ["name", "department", "salary"]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(employee_records)


print("Created employees_updated.csv")

#output

'''
{'name': 'Alice', 'department': 'Engineering', 'salary': '70000'}
{'name': 'Bob', 'department': 'Sales', 'salary': '55000'}
{'name': 'Carol', 'department': 'Engineering', 'salary': '80000'}
{'name': 'Dave', 'department': 'HR', 'salary': '50000'}
{'name': 'Eve', 'department': 'Sales', 'salary': '60000'}
Total salary by department: {'Engineering': 150000.0, 'Sales': 115000.0, 'HR': 50000.0}
Created employees_updated.csv
'''