num=int(input("Enter the number to be checked whether it is a prime or not:"))

def is_prime(num):
    count=0
    for i in range(1,num+1):
        if num % i==0:
            count=count+1

    if count==2:
        print(f"the given number {num} is prime")
    else:
         print(f"the given number {num} is not prime")
        

is_prime(num)

# OUTPUT 
# Enter the number to be checked whether it is a prime or not:17
# the given number 17 is prime

limit=30
def primes_upto_limit(limit):
    for i in range(2,limit+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count=count+1
        
        if count==2:
            print(f"{i}",end=" ")

primes_upto_limit(limit)

# OUTPUT

# 2 3 5 7 11 13 17 19 23 29 