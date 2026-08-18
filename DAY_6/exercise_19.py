value = "abc123"

try:
    number = int(value)
    print("Converted successfully:", number)
except ValueError:
    print(f"Error: '{value}' cannot be converted to an integer.")
