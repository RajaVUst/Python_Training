def is_even_print(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")

def is_even_return(n):
    if n%2==0:
        return True
    else:
        return False

n=int(input("Enter a number: "))

is_even_print(n)
print(is_even_return(n))

"""Enter a number: 7
Odd
False"""