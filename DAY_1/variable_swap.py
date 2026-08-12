a = 5
b = 10

# Method 1: Temporary variable
temp = a
a = b
b = temp

print(f"After method 1: a = {a}, b = {b}")

# Reset values
a = 5
b = 10

# Method 2: Multiple assignment
a, b = b, a

print(f"After method 2: a = {a}, b = {b}")