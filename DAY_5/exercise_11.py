contact = {
    "name": "Reni",
    "email": "reni@example.com",
    "phone": "9876543210"
}

print(contact["name"])
print(contact["email"])
print(contact["phone"])

contact["city"] = "Bangalore"
print("After adding city:", contact)

contact["phone"] = "1234567890"
print("After updating phone:", contact)

contact.pop("email")
print("After removing email:", contact)
