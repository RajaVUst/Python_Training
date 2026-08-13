# 20: Print primes in a range 
for i in range(2,51):
    if i%2==0:
        continue
    for j in range (3,int(i**0.5)+1,2):
        if i%j==0:
            break
    else:
        print(i)