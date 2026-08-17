contact = {
    "name": "Shashi",
    "email": "Shashi@example.com",
    "phone": "9876543210"
}

print("Name:", contact["name"])
print("Email:", contact["email"])
print("Phone:", contact["phone"])

contact["city"] = "Trivandrum"

contact["phone"] = "9998887776"

contact.pop("email")

print(contact)

# Output:
"""
Name: Shashi
Email: Shashi@example.com
Phone: 9876543210

{'name': 'Shashi', 'phone': '9998887776', 'city': 'Trivandrum'}   
"""