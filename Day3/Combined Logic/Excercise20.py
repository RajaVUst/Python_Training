#Print primes in a range
for n in range(2, 51):
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    if count == 2:
        print(n,end=" ")