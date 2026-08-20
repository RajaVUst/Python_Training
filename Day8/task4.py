# Task 4.1 - try/except/finally Basics
def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Dividing with zero!!")
        return None
    except TypeError:
        print("type mismatch")
        return None
    finally:
        print("Operation attempted")

safe_divide(4,0)    # Dividing with zero!!
safe_divide(6,"7")  # type mismatch
                    # Operation attempted

# Task 4.2 - Exception Handling: Concept Check
""" Catching with specific except gives what error we are handling
    rathar than bare except which hides the error making debugging difficult """

""" finally is useful in situations where we need it to be excuted 
    compulsory irrespective of result or error such as closing db connection """

""" Catching separately allows us to handle differnt exception differently
    like different code or logging to user specifically """

# Task 4.3 - Capstone: Robust CSV -> JSON Converter
import csv, json
customer_totals = {}
statuses = set()

try:
    with open("orders.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start=2):
            try:
                amount = float(row["amount"])

            except (TypeError, ValueError):
                print(
                    f"Warning: Invalid amount on row {row_number} "
                    f"for customer {row.get('customer')}. Skipping."
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
        "statuses": sorted(statuses)
    }

    with open("order_summary.json", "w") as file:
        json.dump(summary, file, indent=2)

    print("Created: order_summary.json")
    print("Customer totals:", customer_totals)
    print("Statuses:", statuses)

except FileNotFoundError:
    print("Error: orders.csv was not found.")

except Exception as error:
    print("Unexpected error:", error)

finally:
    print("Conversion attempt finished")

# Output -> 
# Warning: Invalid amount on row 5 for customer Mohan. Skipping.
# Warning: Invalid amount on row 9 for customer Rana. Skipping.
# Created: order_summary.json
# Customer totals: {'Alice': 77000.0, 'Shiva': 100000.0, 'Bob': 55000.0, 'Eva': 104500.0, 'David': 60000.0}
# Statuses: {'completed', 'pending'}
# Conversion attempt finished