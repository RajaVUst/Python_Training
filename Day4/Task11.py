def is_even_print(n):
    """This funtion is for 
    printing the even/odd"""
    if n%2==0:
        print("Even")
    else:
        print("odd")
def is_even_return(n):
    """this function is to return
      True/false for even/odd numbers"""
    if n%2==0:
        return True
    else:
        return False

help(is_even_return)
help(is_even_print)

#Output
"""
this function is to return
    True/false for even/odd numbers

This funtion is for
    printing the even/odd
"""