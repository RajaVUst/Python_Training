usd = float(input("Enter amount in USD: "))
rate = float(input("Enter USD to INR conversion rate: "))

inr = usd * rate

print(f"USD: ${usd:,.2f}")
print(f"INR: ₹{inr:,.2f}")