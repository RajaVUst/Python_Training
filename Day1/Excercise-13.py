# Exercise 13 — Currency Converter
usd = float(input("Enter amount in USD: "))
rate = float(input("Enter conversion rate: "))
 
inr = usd * rate
print(f"${usd:,.2f} = ₹{inr:,.2f}")