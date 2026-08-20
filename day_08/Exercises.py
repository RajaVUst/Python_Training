# Task 1.1 — Inventory Tracker

items = ["pen", "notebook", "pen", "eraser", "notebook", "pen", "stapler"]

item_list = list(items)
first_batch = tuple(items[:3])
unique_items = set(items)

item_counts = {}
for item in items:
    item_counts[item] = item_counts.get(item, 0) + 1

print("List:", item_list)
print("Tuple:", first_batch)
print("Set:", unique_items)
print("Dictionary:", item_counts)

print()


# Task 1.2 — Comprehensions Rewrite

squares = [n * n for n in range(1, 21) if n % 2 == 0]

word_lengths = {
    word: len(word)
    for word in ["python", "java", "c", "kotlin"]
}

unique_vowels = {
    ch
    for ch in "the quick brown fox jumps over the lazy dog"
    if ch in "aeiou"
}

print("Squares:", squares)
print("Word lengths:", word_lengths)
print("Unique vowels:", unique_vowels)

print()


# Task 1.3 — Nested Comprehension Challenge

sentences = [
    "the sky is blue",
    "python is fun",
    "list comprehensions are handy"
]

long_words = [
    word
    for sentence in sentences
    for word in sentence.split()
    if len(word) > 2
]

unique_words = {
    word.lower()
    for sentence in sentences
    for word in sentence.split()
}

print("Words longer than 2 characters:", long_words)
print("Unique words:", unique_words)

# A nested comprehension becomes less readable when it has several
# nested levels or complicated conditions. In that case, normal loops
# are easier to understand.

print()


# Task 2.1 — Student Grade Book

students = {
    "alice": [88, 92, 79],
    "bob": [65, 70, 68],
    "carol": [95, 91, 89],
    "dave": []
}

averages = {
    name: sum(grades) / len(grades) if grades else None
    for name, grades in students.items()
}

above_80 = {
    name
    for name, grades in students.items()
    if grades and all(grade > 80 for grade in grades)
}

sorted_students = sorted(
    averages.items(),
    key=lambda x: x[1] if x[1] is not None else float("-inf"),
    reverse=True
)

print("Average grades:", averages)
print("Students with every grade above 80:", above_80)
print("Sorted students:", sorted_students)

print()


# Task 2.2 — Set Operations: Access Control

team_a = {"figma", "jira", "slack", "github"}
team_b = {"jira", "slack", "notion", "vscode"}

common_tools = team_a & team_b
only_team_a = team_a - team_b
combined_tools = team_a | team_b
symmetric_difference = team_a ^ team_b

print("Common tools:", common_tools)
print("Only Team A:", only_team_a)
print("Combined toolset:", combined_tools)
print("Symmetric difference:", symmetric_difference)

def access_report(team_a, team_b):
    return {
        "common": team_a & team_b,
        "only_team_a": team_a - team_b,
        "combined": team_a | team_b,
        "symmetric_difference": team_a ^ team_b
    }

print("Access report:", access_report(team_a, team_b))

print()


# Task 2.3 — Mutability Trap

def add_item(item, basket=[]):
    basket.append(item)
    return basket

print(add_item("apple"))
print(add_item("banana"))

def add_item_fixed(item, basket=None):
    if basket is None:
        basket = []

    basket.append(item)
    return basket

print(add_item_fixed("apple"))
print(add_item_fixed("banana"))

scores = [80, 90]

def add_score(scores, new_score):
    scores.append(new_score)
    return scores

print(add_score(scores, 100))
print("Original scores:", scores)

print()


# Task 3.1 — Basic Read/Write

log_lines = [
    "INFO: Application started",
    "INFO: User logged in",
    "INFO: Inventory loaded",
    "WARNING: Low stock for pens",
    "INFO: Application finished"
]

with open("log.txt", "w", encoding="utf-8") as file:
    for line in log_lines:
        file.write(line + "\n")

with open("log.txt", "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"{line_number}: {line.strip()}")

file = open("log.txt", "r", encoding="utf-8")
print(file.read())
file.close()

with open("log.txt", "a", encoding="utf-8") as file:
    file.write("INFO: Appended log entry\n")

print()


# Task 3.2 — CSV: Employee Records

import csv

employees = [
    ["Alice", "Engineering", 85000],
    ["Bob", "Sales", 62000],
    ["Carol", "Engineering", 92000],
    ["David", "HR", 58000],
    ["Eva", "Sales", 68000]
]

with open("employees.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "department", "salary"])
    writer.writerows(employees)

employee_records = []

with open("employees.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for employee in reader:
        print(employee)
        employee_records.append(employee)

department_salaries = {}

for employee in employee_records:
    department = employee["department"]
    salary = float(employee["salary"])

    department_salaries[department] = (
        department_salaries.get(department, 0) + salary
    )

print("Total salary per department:", department_salaries)

updated_employees = []

for employee in employee_records:
    updated_employee = employee.copy()
    salary = float(updated_employee["salary"])

    if updated_employee["department"] == "Engineering":
        salary *= 1.10

    updated_employee["salary"] = f"{salary:.2f}"
    updated_employees.append(updated_employee)

with open(
    "employees_updated.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["name", "department", "salary"]
    )
    writer.writeheader()
    writer.writerows(updated_employees)

print()


# Task 3.3 — JSON: Config File

import json

config = {
    "app_name": "InventoryApp",
    "version": 1.2,
    "features": ["export", "search", "notifications"],
    "limits": {
        "max_users": 100,
        "max_items": 5000
    }
}

with open("config.json", "w", encoding="utf-8") as file:
    json.dump(config, file, indent=2)

with open("config.json", "r", encoding="utf-8") as file:
    loaded_config = json.load(file)

print(loaded_config["limits"]["max_users"])

loaded_config["features"].append("dark_mode")

with open("config.json", "w", encoding="utf-8") as file:
    json.dump(loaded_config, file, indent=2)

with open("config.json", "r", encoding="utf-8") as file:
    valid_json = file.read()

corrupted_json = valid_json[:-1]

with open("config_corrupted.json", "w", encoding="utf-8") as file:
    file.write(corrupted_json)

try:
    with open("config_corrupted.json", "r", encoding="utf-8") as file:
        json.load(file)
except json.JSONDecodeError as error:
    print("Caught JSONDecodeError:", error)

with open("config.json", "w", encoding="utf-8") as file:
    json.dump(loaded_config, file, indent=2)

print()


# Task 4.1 — try/except/finally Basics

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Warning: Cannot divide by zero.")
        return None
    except TypeError:
        print("Warning: Invalid types.")
        return None
    finally:
        print("Operation attempted")

print("10 / 2 =", safe_divide(10, 2))
print("10 / 0 =", safe_divide(10, 0))
print('"10" / 2 =', safe_divide("10", 2))

print()


# Task 4.2 — Exception Handling: Concept Check

print("Specific exceptions are better than bare except because they")
print("handle only expected errors and make debugging easier.")
print()
print("finally runs whether an exception occurs or not.")
print("It is useful for cleanup such as closing files or database connections.")
print()
print("Catching FileNotFoundError, PermissionError, and IsADirectoryError")
print("separately allows the program to respond appropriately to each problem.")

print()


# Task 4.3 — Capstone: Robust CSV to JSON Converter

sample_orders = [
    ["order_id", "customer", "amount", "status"],
    ["1001", "Alice", "250.50", "completed"],
    ["1002", "Bob", "125.00", "pending"],
    ["1003", "Alice", "75.25", "completed"],
    ["1004", "Carol", "invalid", "cancelled"],
    ["1005", "Bob", "300.00", "completed"],
    ["1006", "David", "", "pending"],
    ["1007", "Carol", "450.75", "completed"],
    ["1008", "Alice", "100.00", "pending"]
]

with open("orders.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(sample_orders)

customer_totals = {}
statuses = set()
valid_orders = []

try:
    with open("orders.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start=2):
            customer = row["customer"]

            try:
                amount = float(row["amount"])
            except (ValueError, TypeError):
                print(
                    f"Warning: Skipping row {row_number} "
                    f"for customer '{customer}'"
                )
                continue

            customer_totals[customer] = (
                customer_totals.get(customer, 0) + amount
            )

            statuses.add(row["status"])

            valid_orders.append({
                "order_id": row["order_id"],
                "customer": customer,
                "amount": amount,
                "status": row["status"]
            })

    summary = {
        "customer_totals": customer_totals,
        "statuses": sorted(statuses),
        "valid_order_count": len(valid_orders),
        "orders": valid_orders
    }

    with open("orders_summary.json", "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=2)

    print("Conversion successful.")
    print("Customer totals:", customer_totals)
    print("Statuses:", sorted(statuses))
    print("Valid orders:", len(valid_orders))

except FileNotFoundError:
    print("Error: orders.csv was not found.")

except Exception as error:
    print("Unexpected error:", error)

finally:
    print("Conversion attempt finished")