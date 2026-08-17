contact = {"name":"aishu", "email":"aishu@gmail.com", "phone":"9999365491"}
print(contact["name"])
print(contact["email"])
print(contact["phone"])
contact["city"] = "banglore"
contact["phone"] = "8882129388"
contact.pop("email")
print(contact)

# output
# aishu
# aishu@gmail.com
# 9999365491
# {'name': 'aishu', 'phone': '8882129388', 'city': 'banglore'}

