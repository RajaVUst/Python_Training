amount = 850
currency = "USD"
if currency == "USD":
    converted = amount / 85
elif currency == "EUR":
    converted = amount / 95
elif currency == "GBP":
    converted = amount / 110
else:
    converted = None
if converted is not None:
    print(f"{amount} INR = {round(converted, 2)} {currency}")
else:
    print("Invalid currency")