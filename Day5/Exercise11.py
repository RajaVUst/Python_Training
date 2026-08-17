
contact = {"name": "Priya", "email": "priya@example.com", "phone": "9876543210"}
print(contact["name"])
print(contact["email"])
print(contact["phone"])
contact["city"] = "Chennai"
contact["phone"] = "9123456780"
contact.pop("email")
print(contact)

#output
# Priya
# priya@example.com
# 9876543210
# {'name': 'Priya', 'phone': '9123456780', 'city': 'Chennai'}