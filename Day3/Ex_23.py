amount_inr = float(input("Enter amount in INR: "))
currency = input("Enter target currency (USD, EUR, GBP): ").upper()

# Fixed conversion rates
usd_rate = 0.012
eur_rate = 0.011
gbp_rate = 0.0095

if currency == "USD":
    converted = amount_inr * usd_rate
    print(f"Converted amount: {converted:.2f} USD")
elif currency == "EUR":
    converted = amount_inr * eur_rate
    print(f"Converted amount: {converted:.2f} EUR")
elif currency == "GBP":
    converted = amount_inr * gbp_rate
    print(f"Converted amount: {converted:.2f} GBP")
else:
    print("Invalid currency choice.")
