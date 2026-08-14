num=int(input("enter the number:"))
def sum_of_numbers(n):
    if n==0:
        return 0
    
    return n+sum_of_numbers(n-1)

print(f"sum of first {num}={sum_of_numbers(num)}")

# OUTPUT

# enter the number:5
# sum of first 5=15