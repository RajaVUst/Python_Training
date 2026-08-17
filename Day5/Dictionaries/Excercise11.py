# Contact Card
contact = {
    "name": "Rohit",
    "email": "rohit@gmail.com",
    "phone": "9876543210"
}

print(contact["name"])
print(contact["email"])
print(contact["phone"])

contact["city"] = "Mumbai"
contact["phone"] = "9876500000"
contact.pop("email")
print(contact)


# Output:
# Rohit
# rohit@gmail.com
# 9876543210
# {'name': 'Rohit', 'phone': '9876500000', 'city': 'Mumbai'}