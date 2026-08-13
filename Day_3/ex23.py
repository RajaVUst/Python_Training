# 23: Simple currency converter 
amount = float(input("Enter amount in INR: "))
currency = input("Enter target currency (USD, EUR, GBP): ").upper()

if currency == "USD":
    converted = amount / 83
elif currency == "EUR":
    converted = amount / 90
elif currency == "GBP":
    converted = amount / 105
else:
    print("Invalid currency selected.")
    converted = None

if converted is not None:
    print("Converted amount:", round(converted, 2), currency)