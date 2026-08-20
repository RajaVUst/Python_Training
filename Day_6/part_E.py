# Exercise 18: Catch a missing file 

try:
    with open("ghost.txt", 'r')as f:
        content = f.read()
except FileNotFoundError:
    print('file doesnt exsit')  

# output 
# file doesnt exsit

# Exercise 19: Catch a bad conversion 

try:
    num = int(input("enter a integer: "))
except ValueError:
    print('ivalid, enter a whole didgit')

# output 

# enter a integer: 0.33
# ivalid, enter a whole didgit


# Exercise 20: Multiple except blocks 

try:
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the Second number: '))
    result = num1/num2
    print(result)
except ValueError:
    print('Enter a whole number')
except ZeroDivisionError:
    print('Cannot be divisible by zero')        


# Exercise 21: Use else 

try:
    with open("diary.txt", "r") as f:
        content = f.read()

except FileNotFoundError:
    print("File doesn't exist.")

else:
    print("File loaded successfully")
    print("File length:", len(content))

# output
# File loaded successfully
# File length: 114

try:
    with open("diy.txt", "r") as f:
        content = f.read()

except FileNotFoundError:
    print("File doesn't exist.")

else:
    print("File loaded successfully")
    print("File length:", len(content))

finally:
    print('Attempt finished')