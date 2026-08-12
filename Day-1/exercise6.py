bill_amount = float(input("Enter bill amount : "))
people_count = int(input("Enter number of people : "))
is_tipping = input("whether wants to tip or not (yes/no) : ") == "yes"
is_tipping = bill_amount/10 if is_tipping else 0
print(f"Amount to be payed by each person is {bill_amount/people_count + is_tipping/people_count}")