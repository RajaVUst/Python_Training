amount = float(input("Enter amount in USD: "))
rate = float(input("Enter conversion rate: "))
rupees = amount * rate
print(f"USD: ${amount:,.2f}")
print(f"INR: ₹{rupees:,.2f}")