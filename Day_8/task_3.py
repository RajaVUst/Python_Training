# Task 3.1 — Basic Read/Write

logs = [
    "INFO: Application started",
    "INFO: User logged in",
    "WARNING: Low disk space",
    "ERROR: Failed to save file",
    "INFO: Application closed"
]

with open("log.txt", "w") as file:
    for log in logs:
        file.write(log + "\n")

# read file back and print line numbers 

with open("log.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"{line_number}: {line.strip()}")

# manual open / close and forgetting to close 

file = open("log.txt", "w")

file.write("INFO: Application started\n")
file.write("INFO: User logged in\n")

# the os keeps the file open longer than necessary 
# other programmer may unable to acccess or modify 
new_logs = [
    "INFO: New session started",
    "INFO: Backup completed"
]

with open("log.txt", "a") as file:
    for log in new_logs:
        file.write(log + "\n")


# Task 3.2 — CSV: Employee Records

import csv
employees = [
    ["Alice", "Engineering", 90000],
    ["Bob", "Sales", 65000],
    ["Carol", "Engineering", 95000],
    ["David", "HR", 60000],
    ["Eve", "Sales", 70000]
]

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "department", "salary"])
    writer.writerows(employees)
employee_records = []
print("Employees:")
with open("employees.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["salary"] = float(row["salary"])
        employee_records.append(row)
        print(row)
department_totals = {}
for employee in employee_records:
    dept = employee["department"]
    salary = employee["salary"]
    department_totals[dept] = department_totals.get(dept, 0) + salary
print("\nTotal Salary by Department:")
print(department_totals)
for employee in employee_records:
    if employee["department"] == "Engineering":
        employee["salary"] *= 1.10
with open("employees_updated.csv", "w", newline="") as file:
    fieldnames = ["name", "department", "salary"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for employee in employee_records:
        writer.writerow({
            "name": employee["name"],
            "department": employee["department"],
            "salary": round(employee["salary"], 2)
        })

print("\nemployees_updated.csv created successfully!")

# Output 

# Employees:
# {'name': 'Alice', 'department': 'Engineering', 'salary': 90000.0}
# {'name': 'Bob', 'department': 'Sales', 'salary': 65000.0}
# {'name': 'Carol', 'department': 'Engineering', 'salary': 95000.0}
# {'name': 'David', 'department': 'HR', 'salary': 60000.0}
# {'name': 'Eve', 'department': 'Sales', 'salary': 70000.0}

# Total Salary by Department:
# {'Engineering': 185000.0, 'Sales': 135000.0, 'HR': 60000.0}

# employees_updated.csv created successfully!

# Task 3.3 — JSON: Config File  

import json

# ----------------------------------
# Original configuration
# ----------------------------------

config = {
    "app_name": "InventoryApp",
    "version": 1.2,
    "features": ["export", "search", "notifications"],
    "limits": {
        "max_users": 100,
        "max_items": 5000
    }
}
with open("config.json", "w") as file:
    json.dump(config, file, indent=2)

print("config.json created.")
with open("config.json", "r") as file:
    loaded_config = json.load(file)

print("Max users:", loaded_config["limits"]["max_users"])
loaded_config["features"].append("dark_mode")

with open("config.json", "w") as file:
    json.dump(loaded_config, file, indent=2)

print("Updated config saved.")

#output 

# employees_updated.csv created successfully!
# config.json created.
# Max users: 100
# Updated config saved.

#Task 4.1 — try/except/finally Basics

def safe_divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print('division by zero is not allowed')
        return None
    except TypeError:
        print('Invalid types provided')
        return None
    finally:
        print('operations attempted')
print(safe_divide(2,0)) 
