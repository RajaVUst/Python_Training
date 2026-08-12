total_bill = float(input("Enter total bill: "))
number_of_people = int(input("Enter number of people: "))

#wants to add a 10% tip or not
wants_tip = input("Do you want to add 10% tip? (yes/no): ").lower()=="yes"

#the tip
tip = total_bill * 0.10 if wants_tip else 0

#final bill
final_bill = total_bill + tip

#each person's share
share = final_bill / number_of_people

#each person's share
print(f"Each person's share: {share:.2f}")