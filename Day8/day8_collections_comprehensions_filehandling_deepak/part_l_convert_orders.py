import csv, json

def create_sample_orders_csv(path):
    rows = [
        {"order_id": "1001", "customer": "alice", "amount": "120.50", "status": "shipped"},
        {"order_id": "1002", "customer": "bob", "amount": "75.00", "status": "pending"},
        {"order_id": "1003", "customer": "alice", "amount": "not_a_number", "status": "shipped"},
        {"order_id": "1004", "customer": "carol", "amount": "300.00", "status": "delivered"},
        {"order_id": "1005", "customer": "bob", "amount": "", "status": "cancelled"},
        {"order_id": "1006", "customer": "dave", "amount": "45.25", "status": "pending"},
        {"order_id": "1007", "customer": "carol", "amount": "60.10", "status": "shipped"},
        {"order_id": "1008", "customer": "alice", "amount": "15.00", "status": "delivered"},
        {"order_id": "1009", "customer": "eve", "amount": "99.99", "status": "pending"},
    ]
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["order_id", "customer", "amount", "status"])
        writer.writeheader()
        writer.writerows(rows)


def convert_orders(csv_path, json_path):
    totals, statuses, skipped = {}, set(), 0
    try:
        with open(csv_path, "r", newline="") as f:
            for row in csv.DictReader(f):
                try:
                    amount = float(row["amount"])
                except (ValueError, TypeError):
                    print(f"Skipping row for {row['customer']} (order {row['order_id']}): {row['amount']!r}")
                    skipped += 1
                    continue
                totals[row["customer"]] = totals.get(row["customer"], 0) + amount
                statuses.add(row["status"])
        summary = {"totals_per_customer": totals, "distinct_statuses": sorted(statuses), "rows_skipped": skipped}
        with open(json_path, "w") as f:
            json.dump(summary, f, indent=2)
        print(summary)
    except FileNotFoundError:
        print(f"Error: could not find {csv_path}.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Conversion attempt finished.")


create_sample_orders_csv("orders.csv")
convert_orders("orders.csv", "orders_summary.json")
convert_orders("missing.csv", "unused.json")