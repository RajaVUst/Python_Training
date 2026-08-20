import csv

employees = [
    {"name": "Alice", "department": "Engineering", "salary": 70000},
    {"name": "Bob", "department": "Sales", "salary": 55000},
    {"name": "Carol", "department": "Engineering", "salary": 82000},
    {"name": "Dave", "department": "Marketing", "salary": 60000},
    {"name": "Eve", "department": "Sales", "salary": 58000},
]

with open("employees.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "department", "salary"])
    for e in employees:
        writer.writerow([e["name"], e["department"], e["salary"]])

with open("employees.csv", "r", newline="") as f:
    rows = list(csv.DictReader(f))
    for r in rows:
        print(dict(r))

dept_totals = {}
for r in rows:
    dept_totals[r["department"]] = dept_totals.get(r["department"], 0) + float(r["salary"])
print(dept_totals)

with open("employees_updated.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "department", "salary"])
    for r in rows:
        salary = float(r["salary"])
        if r["department"] == "Engineering":
            salary *= 1.10
        writer.writerow([r["name"], r["department"], round(salary, 2)])
# Output:
# {'name': 'Alice', 'department': 'Engineering', 'salary': '70000'}
# {'name': 'Bob', 'department': 'Sales', 'salary': '55000'}
# {'name': 'Carol', 'department': 'Engineering', 'salary': '82000'}
# {'name': 'Dave', 'department': 'Marketing', 'salary': '60000'}
# {'name': 'Eve', 'department': 'Sales', 'salary': '58000'}
# {'Engineering': 152000.0, 'Sales': 113000.0, 'Marketing': 60000.0}
# employees_updated.csv -> Alice 77000.0, Bob 55000.0, Carol 90200.0, Dave 60000.0, Eve 58000.0