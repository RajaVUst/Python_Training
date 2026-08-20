import csv
import json


def create_sample_orders(path):
    orders = [
        ["1001", "Alice", "120.50", "completed"],
        ["1002", "Bob", "75.00", "pending"],
        ["1003", "Alice", "invalid", "cancelled"],
        ["1004", "Carol", "210.25", "completed"],
        ["1005", "Bob", "", "pending"],
        ["1006", "Alice", "99.99", "completed"],
        ["1007", "Dave", "50.00", "shipped"],
        ["1008", "Carol", "130.75", "shipped"]
    ]

    with open(
        path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "order_id",
            "customer",
            "amount",
            "status"
        ])

        writer.writerows(orders)


def convert_orders(csv_path, json_path):
    customer_totals = {}
    statuses = set()
    valid_orders = []

    try:
        with open(
            csv_path,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row_number, row in enumerate(
                reader,
                start=2
            ):
                try:
                    amount = float(row["amount"])

                except (ValueError, TypeError):
                    print(
                        f"Warning: invalid amount on row "
                        f"{row_number} for customer "
                        f"{row.get('customer', 'unknown')}. "
                        f"Row skipped."
                    )

                    continue

                customer = row["customer"]
                status = row["status"]

                customer_totals[customer] = (
                    customer_totals.get(customer, 0)
                    + amount
                )

                statuses.add(status)

                valid_orders.append({
                    "order_id": row["order_id"],
                    "customer": customer,
                    "amount": amount,
                    "status": status
                })

        summary = {
            "valid_order_count": len(valid_orders),

            "total_amount_per_customer": {
                customer: round(total, 2)
                for customer, total
                in customer_totals.items()
            },

            "distinct_statuses": sorted(statuses)
        }

        with open(
            json_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(summary, file, indent=2)

        print(f"Summary written to {json_path}")

    except FileNotFoundError:
        print(f"Error: {csv_path} was not found.")

    except Exception as error:
        print("Unexpected error:", error)

    finally:
        print("Conversion attempt finished")


create_sample_orders("orders.csv")

convert_orders(
    "orders.csv",
    "orders_summary.json"
)


#output
'''
Warning: invalid amount on row 4 for customer Alice. Row skipped.
Warning: invalid amount on row 6 for customer Bob. Row skipped.
Summary written to orders_summary.json
Conversion attempt finished
'''