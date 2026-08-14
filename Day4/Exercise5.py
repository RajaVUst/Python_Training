def is_even_print(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

def is_even_return(n):
    if n % 2 == 0:
        return True
    else:
        return False

is_even_print(7)
print(is_even_return(7))

# Output:
# Odd
# False
