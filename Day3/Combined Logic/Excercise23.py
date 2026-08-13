#Simple currency converter
amount = float(input("Enter amount in INR: "))
currency = input("Enter currency (USD/EUR/GBP): ")

if currency == "USD":
    result = amount / 85
    print("USD =", round(result, 2))

elif currency == "EUR":
    result = amount / 100
    print("EUR =", round(result, 2))

elif currency == "GBP":
    result = amount / 115
    print("GBP =", round(result, 2))

else:
    print("Invalid currency")