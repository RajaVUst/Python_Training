# Exercise 10 - Formatted Product Label
name = "Notebook"
price = 149.0
in_stock = True

print(
    f"{name} - ₹{price:.2f} "
    f"({'In Stock' if in_stock else 'Out of Stock'})"
)