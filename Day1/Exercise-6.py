# Exercise 6 — Restaurant Bill Splitter
bill_amount = float(input("Enter total bill amount: "))
people_count = int(input("Enter number of people: "))
add_tip = (input("Add 10% tip? (yes/no): ") == "yes")

if add_tip:
    bill_amount = bill_amount * 1.10

per_person_share = bill_amount / people_count
print(f"Each person pays: {per_person_share:.2f}")