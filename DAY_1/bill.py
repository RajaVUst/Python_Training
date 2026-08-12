bill = float(input("Enter the total bill amount: "))
people = int(input("Enter the number of people: "))
tip_choice = input("Do you want to add a 10% tip? (yes/no): ").lower()

if tip_choice == "yes":
    bill += bill * 0.10

share = bill / people

print(f"Each person's share: ₹{share:.2f}")