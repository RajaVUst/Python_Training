import csv
import json



totals = {}
statuses = set()

try:
    with open("orders.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                amount = float(row["amount"])
            except (ValueError, TypeError):
                print(
                    f"Warning: Invalid amount for row {row['order_id']} "
                    f"(customer: {row['customer']}). Skipping row."
                )
                continue

            customer = row["customer"]
            status = row["status"]

            # Group total amount per customer
            totals[customer] = totals.get(customer, 0) + amount

            # Store distinct statuses
            statuses.add(status)

    summary = {
        "total_amount_per_customer": totals,
        "distinct_statuses": sorted(statuses)
    }

    # Write final summary to JSON
    with open("orders_summary.json", "w") as file:
        json.dump(summary, file, indent=4)

    print("Summary successfully written to orders_summary.json")

except FileNotFoundError:
    print("Error: orders.csv was not found.")

except Exception as e:
    print(f"Unexpected error: {e}")

finally:
    print("Conversion attempt finished")