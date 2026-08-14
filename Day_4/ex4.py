res=0
def multiply(a,b):
    global res
    res=a*b
    return res

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

print(multiply(a,b))

#Output

"""Enter first number4
Enter second number3
12"""