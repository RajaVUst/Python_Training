amount = float(input("Enter amount in USD: "))
conversion_rate = float(input("Enter conversion rate (USD to INR): "))

ind_rupee = amount * conversion_rate

print(f"USD: ${amount:,.2f}")
print(f"INR: ₹{ind_rupee:,.2f}")