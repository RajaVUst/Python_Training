# Exercise 7 - Variable Swap
a = 5
b = 10

# Method 1
temp = a
a = b
b = temp

print("After Method 1")
print(f"a = {a}")
print(f"b = {b}")

# Method 2
a, b = b, a

print("After Method 2")
print(f"a = {a}")
print(f"b = {b}")
