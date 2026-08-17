contact = { "name": "Reni","email": "reni@example.com","phone": "9876543210" }

for key in contact:
    print(f"{key} : {contact[key]}")

contact["city"] = "Trivandrum"
contact["phone"] = "9998887776"
removed_email = contact.pop("email")

print("\nUpdated contact:", contact)
print("Removed email:", removed_email)

"""
Output->
name : Reni
email : reni@example.com
phone : 9876543210

Updated contact: {'name': 'Reni', 'phone': '9998887776', 'city': 'Trivandrum'}
Removed email: reni@example.com
"""