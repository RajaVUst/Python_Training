a = 5
b = 10

#method 1: using a temporary variable
temp = a
a = b
b = temp

print(f"Method 1: a = {a}, b = {b}")

#reset the values
a = 5
b = 10

#method 2: using multiple assignment shortcut
a, b = b, a

print(f"Method 2: a = {a}, b = {b}")