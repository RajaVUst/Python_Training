import csv
import json
 
# Task 4.1 - try/except/finally Basics
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Warning: Cannot divide by zero")
        return None
    except TypeError:
        print("Warning: Invalid data type")
        return None
    finally:
        print("Operation attempted")
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("10", 2))
print()
#  Output:
''' Operation attempted
 5.0
 Warning: Cannot divide by zero
 Operation attempted
 None
 Warning: Invalid data type
 Operation attempted
 None'''
 
 
# Task 4.2 - Exception Handling: Concept Check
"""
1. Catching a specific exception handles only the expected error,
   while a bare except catches every exception. Bare except is
   considered bad practice because it can hide unexpected bugs and
   make debugging difficult.
 
2. The finally block always executes whether an exception occurs
   or not. It is useful for cleanup tasks such as closing files,
   releasing resources, or disconnecting from a database.
 
3. Catching FileNotFoundError, PermissionError, and
   IsADirectoryError separately allows a program to respond
   appropriately to each problem. A generic Exception provides
   less information and makes troubleshooting harder.
"""
 
 
# Task 4.3 - Capstone: Robust CSV to JSON Converter
orders = [
    ["101", "Alice", "250.50", "Completed"],
    ["102", "Bob", "180.00", "Pending"],
    ["103", "Alice", "90.75", "Completed"],
    ["104", "Carol", "", "Pending"],
    ["105", "David", "abc", "Cancelled"],
    ["106", "Bob", "120.25", "Completed"],
    ["107", "Emma", "300.00", "Completed"],
    ["108", "Alice", "75.00", "Pending"]
]
with open("orders.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["order_id", "customer", "amount", "status"])
    writer.writerows(orders)
try:
    customer_totals = {}
    statuses = set()
    with open("orders.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                amount = float(row["amount"])
            except ValueError:
                print(
                    f"Warning: Invalid amount for customer "
                    f"{row['customer']} in order {row['order_id']}"
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
    }
    with open("orders_summary.json", "w") as file:
        json.dump(summary, file, indent=2)
    print("Summary written to orders_summary.json")
except FileNotFoundError:
    print("Error: orders.csv not found")
except Exception as e:
    print("Unexpected Error:", e)
finally:
    print("Conversion attempt finished")


#  Output:
''' Warning: Invalid amount for customer Carol in order 104
Warning: Invalid amount for customer David in order 105
Summary written to orders_summary.json
Conversion attempt finished'''