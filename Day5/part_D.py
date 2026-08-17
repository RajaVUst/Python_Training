# Exercise 11: Contact Card
contact = {"name": "shabanam", "email": "shabanam@mail.com", "phone": 97653943}
for i in contact.keys():
    print(f"{i} : {contact[i]}")    # name: shabanam, email: shabanam@email.com, phone: 97653943
contact["city"] = "Trivandrum"
contact["phone"] = 7934364
contact.pop("email")        
print(contact)      # {'name': 'shabanam', 'phone': 7934364, 'city': 'Trivandrum'}

# Exercise 12: Word Frequency Counter
text = "the quick brown fox jumps over the lazy dog the fox runs"
dict_words = {}
for word in text.split():
    dict_words[word] = dict_words.get(word, 0) + 1
print(dict_words)   # {'the': 3, 'quick': 1, 'brown': 1, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1, 'runs': 1}

# Exercise 13: Class Roster (Nested Structure)
roster = [{"name":"chitti","scores":[45,86,79]}, {"name":"sundari","scores":[98,50,49]}, {"name":"radha", "scores":[99,90,93]}]
for i in roster:
    print(f"{i["name"]} scored {(sum(i["scores"])/len(i["scores"])):.1f}")
#   Output
# chitti scored 70.0
# sundari scored 65.7
# radha scored 94.0

# Exercise 14: Lookup Table
grade_lookup = {"A":90, "B":80, "C":70, "D":60, "F":50}
score = 84
for key, value in grade_lookup.items():
    if score > value:
        print(key)      # B
        break