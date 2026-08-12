#product properties 

name=input("enter the product name ")

price=float(input("enter the price of the product"))

in_stock=bool(input("True or False"))

print(f"{name}= ₹{price:.2f}({'In Stock'if in_stock else 'out of stock'})")