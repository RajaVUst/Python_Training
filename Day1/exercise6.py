bill = float(input("Enter total bill: "))
people = int(input("Enter number of people: "))

wants_tip = input("Do you want to add 10% tip? (yes/no): ").lower() == "yes"

if wants_tip:
    bill = bill * 1.10
share = bill / people
print(f"Each person's share: ₹{share:.2f}")