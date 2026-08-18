value = "abc"
 
try:
    number = int(value)
    print(number)
except ValueError:
    print("Please enter a valid integer.")
 
# Output:
# Please enter a valid integer.
 