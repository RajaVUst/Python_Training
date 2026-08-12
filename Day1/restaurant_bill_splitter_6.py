total_bill = float(input("Enter the total bill amount :"))
no_people = int(input("Enter the no. of people : "))

wants_tip = input("Do you want to add tip  10 % (yes/no):").lower() == "yes"

tip_amount = total_bill * 0.10 * wants_tip
final_bill = tip_amount + total_bill

share_amount = final_bill / no_people

print(f" Each person share is {share_amount:.2f}")
