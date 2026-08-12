# input the total bill amount and number of people
total_bill = float(input("Enter the total bill amount: "))
n = int(input("Enter the number of people: "))

# ask the user if they want to add a tip
wants_tip = input("Do you want to add a tip? (yes/no): ").lower() == "yes"
tip_percentage = 0.0

# add 10% tip to the total bill if the user wants it
if wants_tip:
    total_bill *= 1.10

# calculate and print each person's share, formatted to two decimal places
share_per_person = total_bill / n
print(f"Each person should pay: ₹{share_per_person:.2f}")