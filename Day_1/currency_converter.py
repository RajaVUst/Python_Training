usd = float(input("Enter amount in US Dollars: "))
rate = float(input("Enter conversion rate (INR per USD): "))
inr = usd * rate
print(f"Equivalent amount in INR: ₹{inr:,.2f}")