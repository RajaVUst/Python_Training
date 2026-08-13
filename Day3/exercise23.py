amount = 100000
currency = "USD"

if currency == "USD":
    converted = amount / 96
elif currency == "EUR":
    converted = amount / 110
elif currency == "GBP":
    converted = amount / 126
else:
    converted = None
    print("Invalid currency")

if converted is not None:
    print(f"{currency}: {round(converted, 2)}")