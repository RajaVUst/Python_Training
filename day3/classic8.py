amount = float(input("Enter amount in INR: "))
currency = input("Enter target currency (USD/EUR/GBP): ").upper()

if currency == "USD":
    converted = amount / 90
    print(f"Converted amount: {converted:.2f} USD")

elif currency == "EUR":
    converted = amount / 105
    print(f"Converted amount: {converted:.2f} EUR")

elif currency == "GBP":
    converted = amount / 120
    print(f"Converted amount: {converted:.2f} GBP")

else:
    print("Invalid currency")