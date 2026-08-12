a = 5
b = 10

temp = a
a = b
b = temp

print(f"a = {a}")
print(f"b = {b}")

#2
a = 5
b = 10

a, b = b, a

print(f"a = {a}")
print(f"b = {b}")