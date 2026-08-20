
import csv

employees = [
    ["Alice", "Engineering", 60000],
    ["Bob", "HR", 45000],
    ["Carol", "Engineering", 70000],
    ["David", "Sales", 50000],
    ["Eve", "Engineering", 65000]
]

# Create employees.csv
with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "department", "salary"])
    writer.writerows(employees)


# Read using DictReader
employee_data = []

with open("employees.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for employee in reader:
        employee_data.append(employee)
        print(employee)

# Output:
# {'name': 'Alice', 'department': 'Engineering', 'salary': '60000'}
# {'name': 'Bob', 'department': 'HR', 'salary': '45000'}
# {'name': 'Carol', 'department': 'Engineering', 'salary': '70000'}
# {'name': 'David', 'department': 'Sales', 'salary': '50000'}
# {'name': 'Eve', 'department': 'Engineering', 'salary': '65000'}


# Total salary per department
department_salary = {}

for employee in employee_data:
    department = employee["department"]
    salary = float(employee["salary"])

    department_salary[department] = (
        department_salary.get(department, 0) + salary
    )

print("Department salaries:", department_salary)

# Output:
# Department salaries:{'Engineering': 195000.0, 'HR': 45000.0, 'Sales': 50000.0}


# Add 10% raise to Engineering employees
updated_employees = []

for employee in employee_data:
    employee = employee.copy()

    if employee["department"] == "Engineering":
        salary = float(employee["salary"])
        salary = salary * 1.10
        employee["salary"] = f"{salary:.2f}"

    updated_employees.append(employee)


# Write employees_updated.csv
with open("employees_updated.csv", "w", newline="") as file:
    fieldnames = ["name", "department", "salary"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(updated_employees)

print("Updated employee file created.")

# Output:
# Updated employee file created.