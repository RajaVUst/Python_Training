
import csv
import json
#Task 3.1 — Basic Read/Write
# Write logs
logs = [
    "Application started\n",
    "User logged in\n",
    "Data loaded successfully\n",
    "Report generated\n",
    "Application closed\n"
]

with open("log.txt", "w") as f:
    f.writelines(logs)

# Read with line numbers
with open("log.txt", "r") as f:
    for line_number, line in enumerate(f, start=1):
        print(f"{line_number}: {line.strip()}")

# Append new log entry
with open("log.txt", "a") as f:
    f.write("Backup completed successfully\n")

print("\nUpdated file contents:")

with open("log.txt", "r") as f:
    for line_number, line in enumerate(f, start=1):
        print(f"{line_number}: {line.strip()}")


#Output
'''1: Application started
2: User logged in
3: Data loaded successfully
4: Report generated
5: Application closed

Updated file contents:
1: Application started
2: User logged in
3: Data loaded successfully
4: Report generated
5: Application closed
6: Backup completed successfully'''


# Task 3.2 - CSV: Employee Records

employees = [
    ["Jay", "Engineering", 60000],
    ["Riki", "HR", 45000],
    ["Top", "Engineering", 70000],
    ["Sean", "Finance", 55000],
    ["Han", "Engineering", 65000]
]

# Create employees.csv
with open("employees.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["name", "department", "salary"])

    for employee in employees:
        writer.writerow(employee)

print("employees.csv created.\n")


# Read with DictReader
print("Employee Records:")

employee_rows = []

with open("employees.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)
        employee_rows.append(row)

print()


# Compute total salary per department
department_totals = {}

for row in employee_rows:
    department = row["department"]
    salary = int(row["salary"])

    department_totals[department] = (
        department_totals.get(department, 0) + salary
    )

print("Salary Totals by Department:")
print(department_totals)
print()


# Give Engineering employees a 10% raise
updated_rows = []

for row in employee_rows:
    if row["department"] == "Engineering":
        salary = int(row["salary"])
        row["salary"] = int(salary * 1.10)

    updated_rows.append(row)

with open("employees_updated.csv", "w", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["name", "department", "salary"]
    )

    writer.writeheader()
    writer.writerows(updated_rows)

print("employees_updated.csv created.\n")

#Output
'''employees.csv created.

Employee Records:
{'name': 'Jay', 'department': 'Engineering', 'salary': '60000'}
{'name': 'Riki', 'department': 'HR', 'salary': '45000'}
{'name': 'Top', 'department': 'Engineering', 'salary': '70000'}
{'name': 'Sean', 'department': 'Finance', 'salary': '55000'}
{'name': 'Han', 'department': 'Engineering', 'salary': '65000'}

Salary Totals by Department:
{'Engineering': 195000, 'HR': 45000, 'Finance': 55000}

employees_updated.csv created.'''

# Task 3.3 - JSON: Config File

config = {
    "app_name": "InventoryApp",
    "version": 1.2,
    "features": ["export", "search", "notifications"],
    "limits": {
        "max_users": 100,
        "max_items": 5000
    }
}

# Write JSON
with open("config.json", "w") as f:
    json.dump(config, f, indent=2)

print("config.json created.\n")


# Read JSON
with open("config.json", "r") as f:
    loaded_config = json.load(f)

print("Max Users:", loaded_config["limits"]["max_users"])
print()


# Add dark_mode feature
loaded_config["features"].append("dark_mode")

with open("config.json", "w") as f:
    json.dump(loaded_config, f, indent=2)

print("dark_mode added and saved.\n")


# Demonstrate JSONDecodeError
print("JSON Decode Error Demo")

try:
    with open("broken_config.json", "r") as f:
        data = json.load(f)

except json.JSONDecodeError as e:
    print("JSON Decode Error:", e)

except FileNotFoundError:
    print("Create a deliberately broken JSON file named 'broken_config.json' to test this.")

#Output
'''config.json created.

Max Users: 100

dark_mode added and saved.

JSON Decode Error Demo'''