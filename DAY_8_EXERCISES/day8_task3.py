import csv
import json

# Task 3.1 - Basic Read/Write
log_lines = [
    "System started",
    "User logged in",
    "Data loaded",
    "Report generated",
    "System shutdown"
]
with open("log.txt", "w") as file:
    for line in log_lines:
        file.write(line + "\n")
with open("log.txt", "r") as file:
    for index, line in enumerate(file, start=1):
        print(f"{index}. {line.strip()}")
file = open("log.txt", "a")
file.write("Manual open example\n")
with open("log.txt", "a") as file:
    file.write("Append mode example\n")
print()
#  Output:
# 1. System started
# 2. User logged in
# 3. Data loaded
# 4. Report generated
# 5. System shutdown



# Task 3.2 - CSV: Employee Records
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
with open("config.json", "w") as file:
    json.dump(config, file, indent=2)
with open("config.json", "r") as file:
    loaded_config = json.load(file)
print("Max Users:", loaded_config["limits"]["max_users"])
loaded_config["features"].append("dark_mode")
with open("config.json", "w") as file:
    json.dump(loaded_config, file, indent=2)
with open("config.json", "w") as file:
    file.write('{"app_name":"InventoryApp"}')
try:
    with open("config.json", "r") as file:
        json.load(file)
except json.JSONDecodeError as e:
    print("Exception Raised:", type(e).__name__)
#  Output:
# Max Users: 100
# Exception Raised: JSONDecodeError
