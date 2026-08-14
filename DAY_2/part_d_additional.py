# Part D - Additional Practice

# --- Exercise 7: Initials Generator ---
full_name = "Reni Kumar"
parts = full_name.split()
initials = parts[0][0] + parts[1][0]
print(f"Initials: {initials}")

print("---")

# --- Exercise 8: Loading Bar ---
print(f"Full   : {'=' * 20}")
print(f"Partial: {'=' * 8 + '-' * 12}")

print("---")

# --- Exercise 9: File Extension Checker ---
filename = "day2_notes.docx"
print(f"Ends with .docx : {filename.endswith('.docx')}")
print(f"Ends with .pdf  : {filename.endswith('.pdf')}")

print("---")

# --- Exercise 10: Find and Replace Report ---
text = "the quick brown fox"
index_found = text.find("brown")
new_text = text.replace("brown", "red")
print(f"Original : {text}")
print(f"Index    : {index_found}")
print(f"New text : {new_text}")

print("---")

# --- Exercise 11: Username Validator (Facts Only) ---
username = "reni_k99"
print(f"Is alphanumeric     : {username.isalnum()}")
print(f"Length              : {len(username)}")
print(f"At least 6 chars    : {len(username) >= 6}")

print("---")

# --- Exercise 12: Title Case vs. Capitalize ---
phrase = "the quick brown fox"
print(f"title()      : {phrase.title()}")
print(f"capitalize() : {phrase.capitalize()}")

print("---")

# --- Exercise 13: Receipt Line Formatter ---
item = "Notebook"
price = 149.0
print(f"{item:<15}|{price:>8.2f}")

print("---")


