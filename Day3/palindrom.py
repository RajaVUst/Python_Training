num = int(input("enter th enumber:"))
original = num
temp = num
reversed_n = 0
while temp > 0:
    reversed_n = reversed_n * 10 + (temp % 10)
    temp = temp // 10
if original == reversed_n:
    print(f"{original} is a palindrome")
else:
    print(f"{original} is not a palindrome")