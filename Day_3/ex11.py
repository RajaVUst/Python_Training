# 11: Sum of first N natural numbers
num=int(input("Enter the n th number to find the sum: "))
sum=0
for i in range(num+1):
    sum=sum+i
print(sum)