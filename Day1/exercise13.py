usd = float(input("Enter amount in USD: "))
conversion_rate = float(input("Enter USD to INR conversion rate: "))

inr = usd * conversion_rate

print(f"₹{inr:,.2f}")