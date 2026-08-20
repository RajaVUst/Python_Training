import csv
import json
import os

base = os.path.dirname(__file__)
orders_path = os.path.join(base, "orders.csv")
summary_path = os.path.join(base, "orders_summary.json")

# Create sample orders.csv (8 rows, 2 with bad/missing amounts)
sample_orders = [
    ["order_id", "customer", "amount", "status"],
    ["1001", "alice",   "250.00",  "shipped"],
    ["1002", "bob",     "89.99",   "pending"],
    ["1003", "carol",   "N/A",     "shipped"],   # bad amount
    ["1004", "alice",   "430.50",  "delivered"],
    ["1005", "david",   "120.00",  "pending"],
    ["1006", "bob",     "",        "cancelled"],  # missing amount
    ["1007", "carol",   "315.75",  "delivered"],
    ["1008", "david",   "60.00",   "shipped"],
]

with open(orders_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(sample_orders)

try:
    total_per_customer = {}
    statuses_seen = set()

    with open(orders_path, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                amount = float(row["amount"])
            except (ValueError, TypeError):
                print(f"WARNING: skipping order {row['order_id']} "
                      f"(customer: {row['customer']}) — invalid amount: {row['amount']!r}")
                continue

            customer = row["customer"]
            total_per_customer[customer] = total_per_customer.get(customer, 0) + amount
            statuses_seen.add(row["status"])

    summary = {
        "total_per_customer": total_per_customer,
        "distinct_statuses": list(statuses_seen),
    }

    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)

    print("\nSummary written to orders_summary.json:")
    print(json.dumps(summary, indent=2))

except FileNotFoundError:
    print("ERROR: orders.csv not found — please create the input file first.")
except Exception as e:
    print(f"ERROR: unexpected problem during conversion — {e}")
finally:
    print("Conversion attempt finished")
