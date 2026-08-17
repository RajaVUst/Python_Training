contact = {
    "name": "Reni",
    "email": "reni@example.com",
    "phone": "9876543210"
}

print(contact["name"])
print(contact["email"])
print(contact["phone"])

contact["city"] = "Bangalore"
contact["phone"] = "9123456789"

contact.pop("email")

print(contact)

# output:
# Reni
# reni@example.com
# 9876543210
# {'name': 'Reni', 'phone': '9123456789', 'city': 'Bangalore'}