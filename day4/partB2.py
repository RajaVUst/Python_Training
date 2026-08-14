n=int(input("Enter the number"))
def is_even(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
        
def even_return(num):
    return num%2==0

is_even(n)
print(f"given num is Even:{even_return(n)}")    

# OUTPUT

# Enter the number5
# Odd
# given num is Even:False