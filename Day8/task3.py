# Task 3.1 - Basic Read/Write
log_lines = [
    "Application started",
    "User logged in",
    "Inventory loaded",
    "Report generated",
    "Application stopped"
]
with open("log.txt","w") as f:
    for line in log_lines:
        f.write(line+ "\n")
with open("log.txt","r") as f:
    for line in f.readlines():
        print(line)             # Application started
                                # User logged in
                                # Inventory loaded
                                # Report generated
                                # Application stopped
file = open("log.txt","w")
file.write("Application Restarted\n")
file.close()    # if doesn't close then it gives memory issues
with open("log.txt","a") as f:
    f.write("Running successfully")

# Task 3.2 - CSV : Employee Records
import csv
employees = [
    {"name": "Alice", "department": "Engineering", "salary": 70000},
    {"name": "Bob", "department": "HR", "salary": 55000},
    {"name": "Carol", "department": "Engineering", "salary": 80000},
    {"name": "David", "department": "Sales", "salary": 60000},
    {"name": "Eva", "department": "Engineering", "salary": 75000}
]
with open("employees.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(["name","department","salary"])
    for emp in employees:
        writer.writerow([emp["name"],emp["department"],emp["salary"]])
departments = {}
with open("employees.csv","r") as f:
    reader = csv.DictReader(f)
    for emp in reader:
        print(emp)
        departments[emp["department"]] = departments.get(emp["department"],0) + float(emp["salary"])
print(departments)          # {'Engineering': 225000.0, 'HR': 55000.0, 'Sales': 60000.0}
for emp in employees:
    if emp["department"] == "Engineering":
        emp["salary"] *= 1.10
with open("employees_updated.csv","w") as f:
    fields = ["name","department","salary"]
    writer = csv.DictWriter(f,fields)
    writer.writeheader()
    writer.writerows(employees)
# Output ->
# {'name': 'Alice', 'department': 'Engineering', 'salary': '70000'}
# {'name': 'Bob', 'department': 'HR', 'salary': '55000'}
# {'name': 'Carol', 'department': 'Engineering', 'salary': '80000'}
# {'name': 'David', 'department': 'Sales', 'salary': '60000'}
# {'name': 'Eva', 'department': 'Engineering', 'salary': '75000'}

# Task 3.3 - JSON: Config File
import json
config = {
    "app_name": "InventoryApp",
    "version": 1.2,
    "features": ["export", "search", "notifications"],
    "limits": {"max_users": 100, "max_items": 5000}
}
with open("config.json","w") as f:
    json.dump(config,f,indent = 2)
with open("config.json","r") as f:
    config = json.load(f)
print(config["limits"]["max_users"])    # 100
config["features"].append("dark_mode")
with open("config.json","w") as f:
    json.dump(config,f,indent = 2)

# JSONDecodeError Expected '}' delimiter