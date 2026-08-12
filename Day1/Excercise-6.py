 
# Exercise 6 — Restaurant Bill Splitter
total_bill = float(input("Enter total bill amount: "))
num_people = int(input("Enter number of people: "))
wants_tip = (input("Add 10% tip? (yes/no): ") == "yes")
 
if wants_tip:
    total_bill = total_bill * 1.10
 
share = total_bill / num_people
print(f"Each person pays: {share:.2f}")