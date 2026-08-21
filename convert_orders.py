
import csv
import json

customer_totals = {}
statuses = set()

try:
    # Read CSV using DictReader inside a with block
    with open("orders.csv", "r", newline="") as file:

        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start=2):

            try:
                amount = float(row["amount"])

            except (ValueError, TypeError):
                print(
                    f"Warning: Invalid amount on row {row_number} "
                    f"for customer {row['customer']}. Skipping record."
                )
                continue

            customer = row["customer"]

            # Group total amount per customer
            customer_totals[customer] = (
                customer_totals.get(customer, 0) + amount
            )

            # Collect distinct statuses
            statuses.add(row["status"])

    # Create summary dictionary
    summary = {
        "customer_totals": customer_totals,
        "statuses": sorted(statuses)
    }

    # Write JSON output
    with open("orders_summary.json", "w") as file:
        json.dump(summary, file, indent=2)

    print("\nSummary written to orders_summary.json")

except FileNotFoundError:
    print("Error: orders.csv was not found.")

except Exception as e:
    print(f"Unexpected error: {e}")

finally:
    print("Conversion attempt finished")
