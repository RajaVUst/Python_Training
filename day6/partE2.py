test_value = "abc"

try:
    number = int(test_value)
    print("Number:", number)
except ValueError:
    print(f"'{test_value}' is not a valid integer.")

# OUTPUT

# 'abc' is not a valid integer.
