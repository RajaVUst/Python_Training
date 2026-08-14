def is_even_print(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")


def is_even_return(n):
    return n % 2 == 0

is_even_print(7)

result = is_even_return(7)
print(result)  

# Output:  
# odd 
# False