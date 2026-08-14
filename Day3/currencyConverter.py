amount_inr = 5000
target_currency = "USD"
usd_rate = 0.012
eur_rate = 0.011
gbp_rate = 0.0095
 
if target_currency == "USD":
    converted = round(amount_inr * usd_rate, 2)
elif target_currency == "EUR":
    converted = round(amount_inr * eur_rate, 2)
elif target_currency == "GBP":
    converted = round(amount_inr * gbp_rate, 2)
else:
    converted = None
if converted is not None:
    print(f"{amount_inr} INR = {converted} {target_currency}")
else:
    print("Unsupported currency")