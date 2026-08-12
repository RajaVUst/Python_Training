# Method 1
a = 10
b = 5

print(a,",",b)

temp = a

a = b
b = temp

print(a,",",b)

# Method 2
a,b = b,a

print(a,",",b)

