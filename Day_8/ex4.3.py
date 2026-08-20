import csv
import json

csv_file = "Day_8/refdoc/orders.csv"
json_file = "Day_8/refdoc/orders_summary.json"

sample_orders = [
    ["order_id", "customer", "amount", "status"],
    [101, "Abrani", 250.50, "completed"],
    [102, "Ram", 100.00, "pending"],
    [103, "Abrani", 75.25, "completed"],
    [104, "Sita", "", "cancelled"],
    [105, "John", "abc", "pending"],
    [106, "Ram", 120.00, "completed"],
    [107, "Priya", 300.00, "shipped"],
    [108, "Abrani", 50.00, "pending"]
]

with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(sample_orders)

try:
    customer_totals = {}
    statuses = set()

    with open(csv_file, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                amount = float(row["amount"])
            except (ValueError, TypeError):
                print(
                    f"Warning: Invalid amount for {row['customer']} "
                    f"(Order ID: {row['order_id']})"
                )
                continue

            customer_totals[row["customer"]] = (
                customer_totals.get(row["customer"], 0) + amount
            )

            statuses.add(row["status"])

    summary = {
        "customer_totals": customer_totals,
        "distinct_statuses": sorted(statuses)
    }

    with open(json_file, "w") as file:
        json.dump(summary, file, indent=2)

    print("orders_summary.json created successfully")

except FileNotFoundError:
    print("Error: orders.csv not found")

except Exception as e:
    print("Unexpected Error:", e)

finally:
    print("Conversion attempt finished")