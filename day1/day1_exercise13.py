# accept amount in dollars and conversion rate to rupees
dollar = float(input("Enter amount in dollars: "))
conversion_rate = float(input("Enter conversion rate to rupees: "))

# convert dollars to rupees and print the result
rupees = dollar * conversion_rate
print(f"{dollar} USD = ₹{rupees:.2f}")