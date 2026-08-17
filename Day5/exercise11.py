contact = {
    "name": "saikiran",
    "email": "saikiran.soma@ustglobal.com",
    "phone": "9876543210"
}

print("Name:", contact["name"])
print("Email:", contact["email"])
print("Phone:", contact["phone"])

contact["city"] = "Hyderabad"
contact["phone"] = "9123456780"
contact.pop("email")

print("Updated contact:", contact)

'''
Name: saikiran
Email: saikiran.soma@ustglobal.com
Phone: 9876543210
Updated contact: {'name': 'saikiran', 'phone': '9123456780', 'city': 'Hyderabad'}
'''