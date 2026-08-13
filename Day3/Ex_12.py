num=1234
sum=0
while num>0:
    digit=num%10
    sum+=digit
    num//=10
print(f"Sum of digits is: {sum}")

