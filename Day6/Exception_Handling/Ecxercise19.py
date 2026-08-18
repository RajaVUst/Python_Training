# Catch a bad conversion

value = input("Enter a number: ")
try:
    number = int(value)
    print("Number:", number)

except ValueError:
    print("Please enter a valid number.")

#Output:
# If users enter the alphabetic it will print 
#Please enter a valid number.