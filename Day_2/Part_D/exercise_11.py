username = "mukheshsai1234"

is_alphanumeric = username.isalnum()
username_length = len(username)
is_at_least_6 = username_length >= 6

print(f"Is alphanumeric: {is_alphanumeric}")
print(f"Length: {username_length}")
print(f"At least 6 characters: {is_at_least_6}")