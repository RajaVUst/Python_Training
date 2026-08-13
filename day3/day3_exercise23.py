# Input amount and target currency
inr = float(input("Enter amount in INR: "))
currency = input("Enter target currency (USD/EUR/GBP): ").upper()

if currency == "USD":
    converted = inr / 80
    print("Converted amount:", round(converted, 2), "USD")

elif currency == "EUR":
    converted = inr / 90
    print("Converted amount:", round(converted, 2), "EUR")

elif currency == "GBP":
    converted = inr / 100
    print("Converted amount:", round(converted, 2), "GBP")

else:
    print("Invalid currency choice.")
