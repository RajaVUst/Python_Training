num=int(input("enter the number:"))
multiply=lambda num:num **3
print(f"The cube of the number is {multiply(num)}")

def cube(num):
    return num**3

answer=cube(num)
print(f"The cube of the number using function is:{answer}")



# Global variable
total_attempts = 0
# Function to increment the global variable
def log_attempt():
    global total_attempts
    total_attempts += 1
# Call the function 3 times
log_attempt()
log_attempt()
log_attempt()
# Print the updated value
print(total_attempts)

#output
#3


#Recursive function

i =int(input("enter the number:"))
def countdown(i):
    if i == 0:
        print("liftoff")
        return
    print(i)
    countdown(i - 1)
countdown(i)


#sum using recursion 
def sum_upto(n):
    if n == 0:
        return 0
    return n + sum_upto(n - 1)
print(sum_upto(5))

#output
#15

