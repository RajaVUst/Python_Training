import csv
import json
sample_orders = [
    ["order_id", "customer", "amount", "status"],
    ["ORD001", "Alice", "250.50", "Completed"],
    ["ORD002", "Bob", "120.00", "Pending"],
    ["ORD003", "Alice", "300.75", "Completed"],
    ["ORD004", "Carol", "450.00", "Shipped"],
    ["ORD005", "Bob", "", "Pending"],
    ["ORD006", "David", "invalid", "Cancelled"],
    ["ORD007", "Carol", "200.00", "Completed"],
    ["ORD008", "Alice", "150.25", "Shipped"],
    ["ORD009", "David", "350.00", "Completed"],
    ["ORD010", "Bob", "175.50", "Shipped"]
]

with open("orders.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(sample_orders)


#  Read CSV and convert it into JSON summary

try:

    customer_totals = {}
    statuses = set()

    with open("orders.csv", "r", newline="") as file:

        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start=2):

            customer = row["customer"]
            amount = row["amount"]
            status = row["status"]

            # Add status to the set
            statuses.add(status)

            try:
                amount = float(amount)

            except (ValueError, TypeError):
                print(
                    f"Warning: Invalid amount in row {row_number} "
                    f"for customer {customer}. Skipping row."
                )
                continue

            customer_totals[customer] = (
                customer_totals.get(customer, 0) + amount
            )


    #  Create final summary

    summary = {
        "customer_totals": customer_totals,
        "statuses": sorted(statuses)
    }


    #  Write summary to JSON

    with open("orders_summary.json", "w") as file:
        json.dump(summary, file, indent=2)


    print("\nConversion completed successfully.")
    print("Customer totals:", customer_totals)
    print("Statuses:", statuses)


#  Handle missing orders.csv

except FileNotFoundError:
    print("Error: orders.csv was not found.")


#  Generic fallback exception

except Exception as error:
    print("Unexpected error occurred:", error)


#  Finally block

finally:
    print("Conversion attempt finished")




#     Warning: Invalid amount in row 6 for customer Bob. Skipping row.
# Warning: Invalid amount in row 7 for customer David. Skipping row.

# Conversion completed successfully.
# Customer totals: {'Alice': 701.5, 'Bob': 295.5, 'Carol': 650.0, 'David': 350.0}
# Statuses: {'Pending', 'Cancelled', 'Completed', 'Shipped'}
# Conversion attempt finished
