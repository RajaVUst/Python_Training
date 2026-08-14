# Part B - Debug the Bug

print("Start")
print("Middle")
print("End")

print("---")

# --- Debug 2: TypeError ---

message = f"I am {age} years old"
print(message)

print("---")

# --- Debug 3: NameError ---

username = "reni_k"
print(f"Welcome, {username}!")

print("---")

# --- Debug 4: IndexError ---

word = "Python"
print(word[5])

print("---")

# --- Debug 5: Silent Logic Bug ---

sentence = "one two three"
word_list = sentence.split(",")
print(f"DEBUG word_list: {word_list}")   # shows the whole string as one item
print(f"Word count (buggy): {len(word_list)}")

# FIX: Split on spaces (default) to correctly separate words.
word_list_fixed = sentence.split()
print(f"Word count (fixed): {len(word_list_fixed)}")
