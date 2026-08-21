items = ["pen", "notebook", "pen", "eraser", "notebook", "pen", "stapler"]
 
arrival_order = list(items)                
first_batch = tuple(items[:3])              
unique_items = set(items)                    
item_counts = {}                            
for item in items:
    item_counts[item] = item_counts.get(item, 0) + 1
 
print(arrival_order)
print(first_batch)
print(unique_items)
print(item_counts)
# Output:
# ['pen', 'notebook', 'pen', 'eraser', 'notebook', 'pen', 'stapler']
# ('pen', 'notebook', 'pen')
# {'stapler', 'notebook', 'pen', 'eraser'}
# {'pen': 3, 'notebook': 2, 'eraser': 1, 'stapler': 1}
 
squares = [n * n for n in range(1, 21) if n % 2 == 0]
word_lengths = {word: len(word) for word in ["python", "java", "c", "kotlin"]}
unique_vowels = {ch for ch in "the quick brown fox jumps over the lazy dog" if ch in "aeiou"}
 
print(squares)
print(word_lengths)
print(unique_vowels)
# Output:
# [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
# {'python': 6, 'java': 4, 'c': 1, 'kotlin': 6}
# {'a', 'u', 'i', 'e', 'o'}
# Note: comprehension was faster to write once familiar; loop reads easier
# once there are multiple conditions or side effects.
 
sentences = ["the sky is blue", "python is fun", "list comprehensions are handy"]
 
long_words = [word for sentence in sentences for word in sentence.split() if len(word) > 2]
unique_words = {word.lower() for sentence in sentences for word in sentence.split()}
 
print(long_words)
print(unique_words)
# Output:
# ['the', 'sky', 'blue', 'python', 'fun', 'list', 'comprehensions', 'are', 'handy']
# {'is', 'handy', 'list', 'are', 'python', 'comprehensions', 'sky', 'blue', 'the', 'fun'}
# Checkpoint: a nested comprehension gets hard to read once you need a 3rd
# level of nesting or more than one 'if' mixed with the nesting.
 
students = {
    "alice": [88, 92, 79],
    "bob": [65, 70, 68],
    "carol": [95, 91, 89],
    "dave": [],
}
 
def safe_average(grades):
    return sum(grades) / len(grades) if grades else None
 
averages = {name: safe_average(g) for name, g in students.items()}
top_students = {name for name, g in students.items() if g and all(x > 80 for x in g)}
sorted_by_avg = sorted(averages.items(), key=lambda p: (p[1] is None, -(p[1] or 0)))
 
print(averages)
print(top_students)
print(sorted_by_avg)
# Output:
# {'alice': 86.33333333333333, 'bob': 67.66666666666667, 'carol': 91.66666666666667, 'dave': None}
# {'carol'}
# [('carol', 91.66666666666667), ('alice', 86.33333333333333), ('bob', 67.66666666666667), ('dave', None)]
 
team_a = {"figma", "jira", "slack", "github"}
team_b = {"jira", "slack", "notion", "vscode"}
 
def access_report(a, b):
    return {"common": a & b, "unique_to_a": a - b, "combined": a | b, "symmetric_difference": a ^ b}
 
print(team_a & team_b)
print(team_a - team_b)
print(team_a | team_b)
print(team_a ^ team_b)
print(access_report(team_a, team_b))
# Output:
# {'slack', 'jira'}
# {'github', 'figma'}
# {'github', 'notion', 'slack', 'vscode', 'figma', 'jira'}
# {'github', 'notion', 'vscode', 'figma'}
# {'common': {'slack', 'jira'}, 'unique_to_a': {'github', 'figma'}, 'combined': {'github', 'notion', 'slack', 'vscode', 'figma', 'jira'}, 'symmetric_difference': {'github', 'notion', 'vscode', 'figma'}}
# Symmetric difference answers: "which tools does only one team have?"
 
def add_item(item, basket=[]):
    basket.append(item)
    return basket
 
print(add_item("apple"))
print(add_item("banana"))
# Output:
# ['apple']
# ['apple', 'banana']   <- mutable default reused across calls, not reset
 
def add_item_fixed(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket
 
print(add_item_fixed("apple"))
print(add_item_fixed("banana"))
# Output:
# ['apple']
# ['banana']
 
def register_user(name, all_users={}):
    all_users[name] = "active"
    return all_users
 
print(register_user("alice"))
print(register_user("bob"))
# Output:
# {'alice': 'active'}
# {'alice': 'active', 'bob': 'active'}   <- alice leaks into bob's call
 
log_lines = ["Server started\n", "User alice logged in\n", "Processed 42 records\n",
             "Warning: low disk space\n", "Server shutting down\n"]
 
with open("log.txt", "w") as f:
    f.writelines(log_lines)
 
with open("log.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}: {line.rstrip()}")
 
# manual open without close (deliberately bad)
bad_file = open("log.txt", "r")
print(bad_file.readline().rstrip())
bad_file.close()   # normally "forgotten" -> file handle leak / unflushed buffer risk
 
with open("log.txt", "a") as f:
    f.write("Additional entry appended after restart\n")
 
with open("log.txt", "r") as f:
    print(f.read())
# Output:
# 1: Server started
# 2: User alice logged in
# 3: Processed 42 records
# 4: Warning: low disk space
# 5: Server shutting down
# Server started
# Server started
# User alice logged in
# Processed 42 records
# Warning: low disk space
# Server shutting down
# Additional entry appended after restart
 
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
 
import json
 
config = {"app_name": "InventoryApp", "version": 1.2,
          "features": ["export", "search", "notifications"],
          "limits": {"max_users": 100, "max_items": 5000}}
 
with open("config.json", "w") as f:
    json.dump(config, f, indent=2)
 
with open("config.json", "r") as f:
    loaded = json.load(f)
print(loaded["limits"]["max_users"])
 
loaded["features"].append("dark_mode")
with open("config.json", "w") as f:
    json.dump(loaded, f, indent=2)
 
with open("config_bad.json", "w") as f:
    f.write(json.dumps(loaded, indent=2)[:-1])   # drop closing brace
 
try:
    with open("config_bad.json", "r") as f:
        json.load(f)
except json.JSONDecodeError as e:
    print(f"Caught json.JSONDecodeError: {e}")
# Output:
# 100
# Caught json.JSONDecodeError: Expecting ',' delimiter: line 14 column 1 (char 198)
 
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print(f"Warning: cannot divide {a} by zero.")
        return None
    except TypeError:
        print(f"Warning: unsupported types for division: {type(a).__name__} and {type(b).__name__}.")
        return None
    finally:
        print("Operation attempted.")
 
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("10", 2))
# Output:
# Operation attempted.
# 5.0
# Warning: cannot divide 10 by zero.
# Operation attempted.
# None
# Warning: unsupported types for division: str and int.
# Operation attempted.
# None
 
Q1. Specific except (e.g. ZeroDivisionError) only catches that one failure
type; bare except: swallows everything — including bugs and
KeyboardInterrupt/SystemExit — hiding real problems.
 
Q2. finally always runs, success or failure — e.g. releasing a manually
opened DB connection back to a pool even if the query raised.
 
Q3. Catching FileNotFoundError/PermissionError/IsADirectoryError separately
lets the program react correctly to WHY it failed instead of showing one
vague generic message.
 
import csv, json
 
def create_sample_orders_csv(path):
    rows = [
        {"order_id": "1001", "customer": "alice", "amount": "120.50", "status": "shipped"},
        {"order_id": "1002", "customer": "bob", "amount": "75.00", "status": "pending"},
        {"order_id": "1003", "customer": "alice", "amount": "not_a_number", "status": "shipped"},
        {"order_id": "1004", "customer": "carol", "amount": "300.00", "status": "delivered"},
        {"order_id": "1005", "customer": "bob", "amount": "", "status": "cancelled"},
        {"order_id": "1006", "customer": "dave", "amount": "45.25", "status": "pending"},
        {"order_id": "1007", "customer": "carol", "amount": "60.10", "status": "shipped"},
        {"order_id": "1008", "customer": "alice", "amount": "15.00", "status": "delivered"},
        {"order_id": "1009", "customer": "eve", "amount": "99.99", "status": "pending"},
    ]
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["order_id", "customer", "amount", "status"])
        writer.writeheader()
        writer.writerows(rows)
 
 
def convert_orders(csv_path, json_path):
    totals, statuses, skipped = {}, set(), 0
    try:
        with open(csv_path, "r", newline="") as f:
            for row in csv.DictReader(f):
                try:
                    amount = float(row["amount"])
                except (ValueError, TypeError):
                    print(f"Skipping row for {row['customer']} (order {row['order_id']}): {row['amount']!r}")
                    skipped += 1
                    continue
                totals[row["customer"]] = totals.get(row["customer"], 0) + amount
                statuses.add(row["status"])
        summary = {"totals_per_customer": totals, "distinct_statuses": sorted(statuses), "rows_skipped": skipped}
        with open(json_path, "w") as f:
            json.dump(summary, f, indent=2)
        print(summary)
    except FileNotFoundError:
        print(f"Error: could not find {csv_path}.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Conversion attempt finished.")
 
 
create_sample_orders_csv("orders.csv")
convert_orders("orders.csv", "orders_summary.json")
convert_orders("missing.csv", "unused.json")
 