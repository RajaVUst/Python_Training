# Method 1: Using a temporary variable
a = 5
b = 10
temp = a
a = b
b = temp
print("Method 1:")
print(f"a = {a}")
print(f"b = {b}")

# Method 2: Python multiple-assignment shortcut
a = 5
b = 10
a, b = b, a
print("Method 2:")
print(f"a = {a}")
print(f"b = {b}")