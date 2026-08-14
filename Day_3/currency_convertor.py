rupees = 100
currency = "USD"

if currency == "USD":
    converted = rupees / 83
elif currency == "EUR":
    converted = rupees / 90
elif currency == "GBP":
    converted = rupees / 105
else:
    print("Invalid currency")
    converted = None

if converted:
    print(round(converted, 2))