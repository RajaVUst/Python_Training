total_bill=float(input("Enter the total bill amount"))

number_of_people=int(input("Enter the number of people sitting"))

wants_tip=input("want to give 10% tip").lower()

if(wants_tip=='yes'):
     with_tip=(total_bill/number_of_people)*0.1
     print(f"each person is {(total_bill/number_of_people)+with_tip:.2f}")
else:
     print(f"each person share without tip:{total_bill/number_of_people:.2f}")

