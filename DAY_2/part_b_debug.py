# Part B - Debug the Bug
# Each section shows the BUGGY code (commented out) and the FIXED version below it.

# --- Debug 1: IndentationError ---
# BUGGY:
#   print("Start")
#     print("Middle")   <-- extra indent causes IndentationError
#   print("End")
#
# FIX: All lines at the same level must have identical indentation.
print("Start")
print("Middle")
print("End")

print("---")

# --- Debug 2: TypeError ---
# BUGGY:
#   age = 24
#   message = "I am " + age + " years old"  <-- can't concatenate str and int
#
# FIX: Use str() to convert int, or use an f-string.
age = 24
message = f"I am {age} years old"
print(message)

print("---")

# --- Debug 3: NameError ---
# BUGGY:
#   username = "reni_k"
#   print(f"Welcome, {usernam}!")  <-- typo: missing 'e' at the end
#
# FIX: Correct the variable name to 'username'.
username = "reni_k"
print(f"Welcome, {username}!")

print("---")

# --- Debug 4: IndexError ---
# BUGGY:
#   word = "Python"
#   print(word[6])  <-- "Python" has indices 0-5; index 6 is out of range
#
# FIX: Use the last valid index (5) or use -1 for the last character.
word = "Python"
print(word[5])

print("---")

# --- Debug 5: Silent Logic Bug ---
# BUGGY:
#   sentence = "one two three"
#   word_list = sentence.split(",")  <-- splits on comma, but there are no commas
#   print(f"Word count: {len(word_list)}")  <-- prints 1 instead of 3
#
# DEBUG: Print word_list to see what split(",") actually returns.
sentence = "one two three"
word_list = sentence.split(",")
print(f"DEBUG word_list: {word_list}")   # shows the whole string as one item
print(f"Word count (buggy): {len(word_list)}")

# FIX: Split on spaces (default) to correctly separate words.
word_list_fixed = sentence.split()
print(f"Word count (fixed): {len(word_list_fixed)}")
