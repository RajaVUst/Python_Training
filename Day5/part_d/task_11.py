contact = {
    "name": "Merin",
    "email": "merin@gmail.com",
    "phone": "9878167210"
}

print(contact["name"])
print(contact["email"])
print(contact["phone"])

contact["city"] = "Chennai"

contact["phone"] = "9876501234"

contact.pop("email")

print(contact)



# Merin
# merin@gmail.com
# 9878167210
# {'name': 'Merin', 'phone': '9876501234', 'city': 'Chennai'}