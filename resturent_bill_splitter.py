total_bill=int(input("enter the total bill amount :"))
total_people=int(input("enter the number of people :"))
print("Willing to pay tip?(YES/NO)")
tip=input()
if(tip=="YES" or tip=="yes"):
    total_bill=((total_bill+(10/100*total_bill))/total_people)
else:
    total_bill=(total_bill/total_people)

print(f"the total amount to be paid {total_bill}")