bill = float(input("Enter Total bill amount: "))
num = int(input("Number of people splitting: "))
tip = (input("want to give 10% tip (yes/no): ") == 'yes')

tip_amount = bill * 0.10 * tip
total = bill + tip_amount
share = total/num

print(f"Each person's share: {share:.2f}")