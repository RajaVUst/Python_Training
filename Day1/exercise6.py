# Exercise 6 - Restaurant Bill Splitter
bill_amount = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))
wants_tip = input("Add 10% tip? (yes/no): ").lower() == "yes"
if wants_tip:
    bill_amount = bill_amount * 1.10
share = bill_amount / people

print(f"Each person pays: ₹{share:.2f}")