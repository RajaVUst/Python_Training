amount = float(input("Enter amount in US Dollars: "))

conversion_rate = float(input("Enter conversion rate: "))

rupees = amount * conversion_rate

print(f"Indian Rupees: ₹{rupees:,.2f}")