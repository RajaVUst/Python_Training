total_bill = float(input("Enter the total bill amount: "))
num_people = int(input("Enter the number of people: "))
tip = input("Add 10% tip? (yes/no): ").strip().lower()
share = total_bill * (1 + 0.1 * (tip == "yes")) / num_people
print(f"Each person should pay: ${share:.2f}")
