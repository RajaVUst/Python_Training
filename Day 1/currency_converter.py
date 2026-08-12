dollars = float(input("Enter amount in US Dollars: "))
conversion_rate = float(input("Enter conversion rate (USD to INR): "))
rupees = dollars * conversion_rate
print(f"Indian Rupees: ₹{rupees:,.2f}")