#Exercise 13  ·  Currency Converter
usd = float(input("Enter the amount in US Dollars: "))
rate = float(input("Enter the conversion rate (INR per USD): "))

inr = usd * rate

print(f"${usd:,.2f} = ₹{inr:,.2f}")