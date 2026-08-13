amount = float(input("Enter amount in Indian Rupees: "))
currency = input("Enter target currency (USD / EUR / GBP): ").upper()

if currency == "USD":
    converted = amount * 0.012
    print(f"{amount} INR = {round(converted, 2)} USD")
elif currency == "EUR":
    converted = amount * 0.011
    print(f"{amount} INR = {round(converted, 2)} EUR")
elif currency == "GBP":
    converted = amount * 0.0094
    print(f"{amount} INR = {round(converted, 2)} GBP")
else:
    print("Invalid currency. Choose USD, EUR, or GBP.")
