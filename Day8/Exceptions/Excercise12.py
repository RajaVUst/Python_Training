# CSV → JSON Converter
import csv
orders = [
    ["101", "Alice", "500", "Completed"],
    ["102", "Bob", "300", "Pending"],
    ["103", "Alice", "250", "Completed"],
    ["104", "Carol", "700", "Shipped"],
    ["105", "Bob", "invalid", "Pending"],
    ["106", "David", "450", "Completed"],
    ["107", "Carol", "", "Cancelled"],
    ["108", "Alice", "600", "Shipped"]
]

with open("Day8/orders.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["order_id", "customer", "amount", "status"])
    writer.writerows(orders)
print("orders.csv created")

# Converts orders.py
import csv
import json

customer_totals = {}
statuses = set()

try:
    with open("Day8/orders.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                amount = float(row["amount"])
            except ValueError:
                print(
                    "Warning:",
                    "Invalid amount for",
                    row["customer"],
                    "Order:",
                    row["order_id"]
                )
                continue
            customer = row["customer"]
            status = row["status"]
            statuses.add(status)
            if customer in customer_totals:
                customer_totals[customer] += amount
            else:
                customer_totals[customer] = amount

    summary = {
        "customer_totals": customer_totals,
        "statuses": list(statuses)
    }

    with open("Day8/orders_summary.json", "w") as file:
        json.dump(summary, file, indent=2)

    print("Conversion successful")

except FileNotFoundError:
    print("orders.csv file was not found")

except Exception as e:
    print("Something went wrong:", e)

finally:
    print("Conversion attempt finished")

# Output:
# Warning: Invalid amount for Bob Order: 105
# Warning: Invalid amount for Carol Order: 107
# Conversion successful
# Conversion attempt finished