contact = {
    "name": "Aron",
    "email": "aron@example.com",
    "phone": "9292092002"
}

print(contact["name"])
print(contact["email"])
print(contact["phone"])

contact["city"] = "Trivandrum"
contact["phone"] = "9998887776"
contact.pop("email")

print(contact)

"""
OUTPUT:
Aron
aron@example.com
9292092002
{'name': 'Aron', 'phone': '9998887776', 'city': 'Trivandrum'}
"""