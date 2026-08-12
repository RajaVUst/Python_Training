bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))

wants_tip = input("Do you want to add a 10% tip? (yes/no): ").lower()

if wants_tip=="yes":
    bill = bill * 1.10

share = bill / people

print(f"Each person's share: ₹{share:.2f}")