def is_even_print(n):
    if n%2==0:
        print(f"{n} is Even")
    else:
        print(f"{n} is Odd")  
is_even_print(7)  



def is_even_return(n):
    if n%2==0:
        return True
    else:
        return False
result=is_even_return(7)  
print(result)  
