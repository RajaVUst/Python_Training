
number=int(input("enter the number"))

cube=lambda x : x ** 3
print(f"cube of {number} using lamda={cube(number)}")


def cube(num):
    print(f"cube of {num}={num**3}")

result=cube(number)

if cube(number)==result:
    print("Correct for both methods")
    
# OUTPUT

# enter the number3
# cube of 3 using lamda=27
# cube of 3=27
# cube of 3=27
# Correct for both methods