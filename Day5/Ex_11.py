contact={"name":"yesh","email":"308331@ust.com","phone":9391702903}
for i in contact.keys():
    print(contact[i])
contact['city']="pune"
contact["phone"]=3282392839
contact.pop('email')
print(contact)
#output
"""
yesh
308331@ust.com
9391702903
{'name': 'yesh', 'phone': 3282392839, 'city': 'pune'}
"""