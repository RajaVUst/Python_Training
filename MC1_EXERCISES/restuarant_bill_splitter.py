bill_amount = float(input("Enter the amount"))
number_of_people = int(input("Enter how many should split"))
wants_tip = input("Want tip(YES/NO)")

tip = wants_tip == "YES"
tip_amount = bill_amount * 0.10 * tip
split_per_person = (bill_amount+tip_amount)/number_of_people

print(f"Each person pays: {split_per_person:.2f}")
