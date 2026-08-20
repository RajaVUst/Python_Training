import csv

employees = [
    ["Alice", "Engineering", 50000],
    ["Bob", "HR", 40000],
    ["Carol", "Engineering", 60000],
    ["David", "Sales", 45000],
    ["Eve", "HR", 42000]
]

with open("Day8/employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "department", "salary"])
    writer.writerows(employees)
print("employees.csv created")


# Read CSV
with open("Day8/employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for employee in reader:
        print(employee)

# Output:
# employees.csv created
# {'name': 'Alice', 'department': 'Engineering', 'salary': '50000'}
# {'name': 'Bob', 'department': 'HR', 'salary': '40000'}
# {'name': 'Carol', 'department': 'Engineering', 'salary': '60000'}
# {'name': 'David', 'department': 'Sales', 'salary': '45000'}
# {'name': 'Eve', 'department': 'HR', 'salary': '42000'}

# Compute total salary per department 
department_salary = {}

with open("Day8/employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for employee in reader:
        department = employee["department"]
        salary = float(employee["salary"])
        if department in department_salary:
            department_salary[department] += salary
        else:
            department_salary[department] = salary

print(department_salary)

# Output: {'Engineering': 110000.0, 'HR': 82000.0, 'Sales': 45000.0}


# Add 10% raising
updated_employees = []
with open("Day8/employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for employee in reader:
        salary = float(employee["salary"])
        if employee["department"] == "Engineering":
            salary = salary * 1.10
        employee["salary"] = salary
        updated_employees.append(employee)

with open("Day8/employees_updated.csv", "w", newline="") as file:
    fieldnames = ["name", "department", "salary"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(updated_employees)

print("Updated file created")

# Output: Updated file created
