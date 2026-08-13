#Exercise 7  ·  Variable Swap  

a = 10
b = 20

# Method 1: temporary variable 
temp = a 
a = b 
b = temp 
print(a, b)

a1 = 70
b1 = 80

# Method 2: Python shortcut 
a1, b1 = b1, a1
print(a1, b1)