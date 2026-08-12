# accept the name, price, and stock status of a product
name = input("Enter product name: ")
price = float(input("Enter product price: "))
in_stock = bool(input("Is the product in stock? (True/False): "))

# print the product details
print(f"{name} - ₹{price:.2f} | In Stock: {in_stock}")