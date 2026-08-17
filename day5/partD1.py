contact={
    "name":"Bonny",
    "email":"Bonny@Email.com",
    "phone":9874923749
}

print(f"name:{contact["name"]}")
print(f"email:{contact["email"]}")
print(f"phone:{contact["phone"]}")

contact["city"]="kochi"
contact["phone"]=9999999999

contact.pop("email")
print(contact)

# OUTPUT

# name:Bonny
# email:Bonny@Email.com
# phone:9874923749
# {'name': 'Bonny', 'phone': 9999999999, 'city': 'kochi'}
