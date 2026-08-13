num=int(input("Enter a number: "))
temp=num
reversed_num=0
while num>0:
    digit=num%10
    reversed_num=reversed_num*10+digit
    num//=10
if temp==reversed_num:
    print(f"{temp} is a palindrome number")
else:
    print(f"{temp} is not a palindrome number")