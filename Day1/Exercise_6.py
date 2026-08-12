#Exercise 6  ·  Restaurant Bill Splitter  
bill = float(input("Enter the total bill amount: "))
people = int(input("Enter the number of people: "))
wants_tip = (input("Add a 10% tip? (yes/no): ").lower() == "yes")

total = bill * 1.10 if wants_tip else bill
share = total / people

print(f"Each person pays: ${share:.2f}")