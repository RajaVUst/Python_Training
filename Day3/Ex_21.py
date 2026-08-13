num=int(input("Enter a number: "))
res=num
for i in range(num-1,0,-1):
    res*=i
if num==0:
    res=1 
print(f"The factorial of {num} is {res}")