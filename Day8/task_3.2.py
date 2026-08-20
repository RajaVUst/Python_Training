
import csv
employees = [
    ["Alice", "Engineering", 75000],
    ["Bob", "HR", 60000],
    ["Carol", "Engineering", 80000],
    ["David", "Finance", 70000],
    ["Eva", "Engineering", 90000]
]


#  Create employees.csv using csv.writer

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "department", "salary"])
    writer.writerows(employees)


#  Read employees.csv using csv.DictReader

employee_records = []

with open("employees.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for employee in reader:
        print(employee)
        employee_records.append(employee)


#  Compute total salary per department

department_salary = {}

for employee in employee_records:
    department = employee["department"]
    salary = float(employee["salary"])

    department_salary[department] = (
        department_salary.get(department, 0) + salary
    )

print("\nTotal salary per department:")

for department, total_salary in department_salary.items():
    print(department, total_salary)


#  Add 10% raise to Engineering employees and create employees_updated.csv

updated_employees = []

for employee in employee_records:
    salary = float(employee["salary"])

    if employee["department"] == "Engineering":
        salary = salary * 1.10

    updated_employees.append([
        employee["name"],
        employee["department"],
        salary
    ])


with open("employees_updated.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "department", "salary"])
    writer.writerows(updated_employees)




#  {'name': 'Alice', 'department': 'Engineering', 'salary': '75000'}
# {'name': 'Bob', 'department': 'HR', 'salary': '60000'}
# {'name': 'Carol', 'department': 'Engineering', 'salary': '80000'}
# {'name': 'David', 'department': 'Finance', 'salary': '70000'}
# {'name': 'Eva', 'department': 'Engineering', 'salary': '90000'}

# Total salary per department:
# Engineering 245000.0
# HR 60000.0
# Finance 70000.0