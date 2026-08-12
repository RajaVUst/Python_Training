name = input("Enter Product name: ")
price = float(input("Enter price"))
in_stock = (input("Is in stock: ") == 'yes')

print(f"{name} ---- ₹{price:.2f} ({'In Stock' if in_stock else 'Out of Stock'})")