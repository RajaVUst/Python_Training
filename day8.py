# Q1
items = ["pen", "notebook", "pen", "eraser", "notebook", "pen", "stapler"]

item_list = items                    # preserves order
item_tuple = tuple(items[:3])        # immutable first batch
item_set = set(items)                # unique items

item_dict = {}
for item in items:
    item_dict[item] = item_dict.get(item, 0) + 1

print(item_list)
print(item_tuple)
print(item_set)
print(item_dict)

# Q2
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

print(squares)
print(word_lengths)
print(unique_vowels)

# Q3
sentences = [
    "the sky is blue",
    "python is fun",
    "list comprehensions are handy"
]

words = [
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

print(words)
print(unique_words)

# Q4
students = {
    "alice": [88, 92, 79],
    "bob": [65, 70, 68],
    "carol": [95, 91, 89]
}

averages = {
    name: (sum(scores) / len(scores) if scores else 0)
    for name, scores in students.items()
}

high_scorers = {
    name
    for name, scores in students.items()
    if scores and all(score > 80 for score in scores)
}

sorted_students = sorted(
    averages.items(),
    key=lambda x: x[1],
    reverse=True
)

print(averages)
print(high_scorers)
print(sorted_students)

# Q5
team_a = {"figma", "jira", "slack", "github"}
team_b = {"jira", "slack", "notion", "vscode"}

print(team_a & team_b)
print(team_a - team_b)
print(team_a | team_b)
print(team_a ^ team_b)

def access_report(team_a, team_b):
    return {
        "common": team_a & team_b,
        "team_a_only": team_a - team_b,
        "all_tools": team_a | team_b,
        "symmetric_difference": team_a ^ team_b
    }

print(access_report(team_a, team_b))

# Q6
def add_item(item, basket=None):
    if basket is None:
        basket = []

    basket.append(item)
    return basket

print(add_item("apple"))
print(add_item("banana"))

# Q7
with open("log.txt", "w") as f:
    f.write("Log 1\n")
    f.write("Log 2\n")
    f.write("Log 3\n")
    f.write("Log 4\n")
    f.write("Log 5\n")

with open("log.txt", "r") as f:
    for index, line in enumerate(f, start=1):
        print(index, line.strip())

with open("log.txt", "a") as f:
    f.write("Log 6\n")

# Q8
import csv

employees = [
    ["Alice", "Engineering", 60000],
    ["Bob", "HR", 45000],
    ["Carol", "Engineering", 70000],
    ["David", "Finance", 55000],
    ["Eva", "HR", 50000]
]

with open("employees.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "department", "salary"])

    for row in employees:
        writer.writerow(row)

department_salary = {}
updated_rows = []

with open("employees.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)

        department = row["department"]
        salary = float(row["salary"])

        department_salary[department] = (
            department_salary.get(department, 0) + salary
        )

        if department == "Engineering":
            salary *= 1.10

        updated_rows.append([
            row["name"],
            department,
            salary
        ])

print(department_salary)

with open("employees_updated.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["name", "department", "salary"])

    for row in updated_rows:
        writer.writerow(row)

# Q9
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

with open("config.json", "w") as f:
    json.dump(config, f, indent=2)

with open("config.json", "r") as f:
    data = json.load(f)

print(data["limits"]["max_users"])

data["features"].append("dark_mode")

with open("config.json", "w") as f:
    json.dump(data, f, indent=2)

# Q10
def safe_divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None

    except TypeError:
        print("Invalid type.")
        return None

    finally:
        print("Operation attempted")

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("10", 2))

# Q11
# Specific exceptions catch only expected errors.
# Bare except catches every exception and hides bugs.

# finally always executes whether an error occurs or not.
# Example: closing files or database connections.

# Catching separate exceptions gives more meaningful handling
# and error messages for each failure type.

# Q12
import csv
import json

try:
    customer_totals = {}
    statuses = set()

    with open("orders.csv", "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            try:
                amount = float(row["amount"])

            except ValueError:
                print(
                    f"Invalid amount for customer {row['customer']}"
                )
                continue

            customer = row["customer"]

            customer_totals[customer] = (
                customer_totals.get(customer, 0) + amount
            )

            statuses.add(row["status"])

    summary = {
        "customer_totals": customer_totals,
        "statuses": list(statuses)