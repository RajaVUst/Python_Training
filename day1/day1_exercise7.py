# Storing values in variables
a=5
b=10

# Method 1: temporary variable
temp = a
a = b
b = temp
print(a, b)

# Method 2: Python shortcut
a, b = b, a
print(a, b)