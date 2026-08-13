#Simple currency converter
amount_inr = float(input("Enter amount in INR: "))
currency = input("Convert to (USD/EUR/GBP): ").upper()
if currency == "USD":
    converted = amount_inr / 83.0
elif currency == "EUR":
    converted = amount_inr / 90.0
elif currency == "GBP":
    converted = amount_inr / 105.0
else:
    converted = None
if converted is not None:
    print(f"{amount_inr} INR = {round(converted, 2)} {currency}")
else:
    print("Unsupported currency")