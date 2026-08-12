bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))
wants_tip = input("Add 10% tip? (yes/no): ").lower() == "yes"

total_bill = bill * (1 + 0.10 * wants_tip)
share_per_person = total_bill / people

print(f"Each person pays: {share_per_person:.2f}")