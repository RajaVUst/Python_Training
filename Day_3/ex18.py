# 18: Palindrome check for an integer 
num=int(input("Enter a number: "))
old_num=num
new_num=0
while num>0:
    new_num=new_num*10+(num%10)
    num=num//10
if new_num==old_num:
    print(f"{old_num} is a palindrome")
else:
    print(f"{old_num} is not a palindrome")