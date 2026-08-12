# Exercise 10 — Formatted Product Label
item_name = "Notebook"
item_price = 149.0
in_stock_status = True

print(f"{item_name} — ₹{item_price:.2f} ({'In Stock' if in_stock_status else 'Out of Stock'})")