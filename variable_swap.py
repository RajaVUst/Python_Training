# By Using Temporray Varible
a=5
b=10
print(f"The value of a before Swapping was:{a}")
print(f"The value of b before Swapping was: {b}")
c=a
a=b
b=c
print(f"The value of a After Swapping is: {a}")
print(f"The value of a After Swapping is:{b}")

# without  Using Temporray Varible

a = 20
b = 30
print(f"The value of a before swapping was: {a}")
print(f"The value of b before swapping was: {b}")
a, b = b, a
print(f"The value of a after swapping is: {a}")
print(f"The value of b after swapping is: {b}")