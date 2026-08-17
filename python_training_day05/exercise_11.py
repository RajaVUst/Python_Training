contact = {
    "name": "Deepa",
    "email": "deepa@example.com",
    "phone": "9876543210"
}

print(contact["name"])
print(contact["email"])
print(contact["phone"])

contact["city"] = "Chennai"

contact["phone"] = "9876501234"

contact.pop("email")

print(contact)



#output:
'''Deepa
deepa@example.com
9876543210
{'name': 'Deepa', 'phone': '9876501234', 'city': 'Chennai'}'''