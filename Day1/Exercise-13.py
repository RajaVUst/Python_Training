# Exercise 13 — Currency Converter
amount_usd = float(input("Enter amount in USD: "))
conversion_rate = float(input("Enter conversion rate: "))

amount_inr = amount_usd * conversion_rate
print(f"${amount_usd:,.2f} = ₹{amount_inr:,.2f}")