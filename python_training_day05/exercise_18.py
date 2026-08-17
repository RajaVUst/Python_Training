products = {
    "apple": 30,
    "banana": 20,
    "orange": 40,
    "mango": 50
}

discounted = {
    product: price * 0.9
    for product, price in products.items()
}

print(discounted)



#output:
'''{'apple': 27.0, 'banana': 18.0, 'orange
': 36.0, 'mango': 45.0}'''