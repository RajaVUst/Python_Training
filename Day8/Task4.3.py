
import csv
import json

orders = [
    ["order_id", "customer", "amount", "status"],
    ["O001", "Alice", "250.50", "Completed"],
    ["O002", "Bob", "150.00", "Pending"],
    ["O003", "Alice", "300.00", "Completed"],
    ["O004", "Carol", "invalid", "Cancelled"],
    ["O005", "Bob", "450.75", "Completed"],
    ["O006", "David", "", "Pending"],
    ["O007", "Carol", "200.00", "Completed"],
    ["O008", "Alice", "125.25", "Pending"]
]

with open("orders.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(orders)


customer_totals = {}
statuses = set()

try:
    with open("orders.csv", "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            customer = row["customer"]
            amount_text = row["amount"]
            status = row["status"]

            statuses.add(status)

            try:
                amount = float(amount_text)

            except (ValueError, TypeError):
                print(
                    f"Warning: Invalid amount for row "
                    f"{row['order_id']} / customer {customer}. Skipping."
                )
                continue

            customer_totals[customer] = (
                customer_totals.get(customer, 0) + amount
            )

    summary = {
        "customer_totals": customer_totals,
        "statuses": sorted(statuses)
    }

    with open("orders_summary.json", "w") as file:
        json.dump(summary, file, indent=2)


    print("Conversion successful.")
    print("Customer totals:", customer_totals)
    print("Statuses:", sorted(statuses))

except FileNotFoundError:
    print("Error: orders.csv was not found.")

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Conversion attempt finished")


# Output:
# Warning: Invalid amount for row O004 / customer Carol. Skipping.
# Warning: Invalid amount for row O006 / customer David. Skipping.
# Conversion successful.
# Customer totals: {
#     'Alice': 675.75,
#     'Bob': 600.75,
#     'Carol': 200.0
# }
# Statuses: ['Cancelled', 'Completed', 'Pending']
# Conversion attempt finished