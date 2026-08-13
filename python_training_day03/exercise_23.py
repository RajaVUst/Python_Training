amount = float(input("Enter amount in INR: "))
currency = input("Enter target currency (USD/EUR/GBP): ").upper()

if currency == "USD":
    converted = amount / 90
    print(f"Amount in USD: {converted:.2f}")

elif currency == "EUR":
    converted = amount / 105
    print(f"Amount in EUR: {converted:.2f}")

elif currency == "GBP":
    converted = amount / 120
    print(f"Amount in GBP: {converted:.2f}")

else:
    print("Invalid currency")