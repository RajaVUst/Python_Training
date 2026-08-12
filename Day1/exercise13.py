# Exercise 13 - Currency Converter
usd = float(input("Enter amount in USD: "))
rate = float(input("Enter conversion rate: "))
inr = usd * rate

print(
    f"USD Amount: ${usd:,.2f}\n"
    f"INR Amount: ₹{inr:,.2f}"
)