import csv

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
# Warning: Invalid amount for customer Carol in order 104
# Warning: Invalid amount for customer David in order 105
# Summary written to orders_summary.json
# Conversion attempt finished