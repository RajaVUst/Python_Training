import csv
import json

customer_totals = {}
statuses = set()

try:
    with open("orders.csv", "r", newline="") as f:
        reader = csv.DictReader(f)

        for row_number, row in enumerate(reader, start=2):
            try:
                amount = float(row["amount"])
            except (ValueError, TypeError):
                print(
                    f"Warning: Invalid amount at row {row_number} "
                    f"for customer {row['customer']}"
                )
                continue

            customer = row["customer"]
            status = row["status"]

            customer_totals[customer] = (
                customer_totals.get(customer, 0) + amount
            )

            statuses.add(status)

    summary = {
        "customer_totals": customer_totals,
        "statuses": list(statuses)
    }

    with open("orders_summary.json", "w") as f:
        json.dump(summary, f, indent=2)

except FileNotFoundError:
    print("orders.csv was not found")

except Exception as e:
    print("Something went wrong:", e)

finally:
    print("Conversion attempt finished")

# OUTPUT

# {
#   "customer_totals": {
#     "Alice": 1000.0,
#     "Bob": 400.0,
#     "Carol": 400.0
#   },
#   "statuses": [
#     "Completed",
#     "Pending"
#   ]
# }