amount_inr = float(input("Enter amount in INR: "))
currency = input("Enter target currency (USD/EUR/GBP): ").upper()
if currency == "USD":
    converted = amount_inr / 83.0
elif currency == "EUR":
    converted = amount_inr / 90.0
elif currency == "GBP":
    converted = amount_inr / 105.0
else:
    print("Invalid currency selected.")
    exit()
print(f"Converted amount: {round(converted, 2)} {currency}")