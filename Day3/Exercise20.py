#Print primes in a range
for candidate in range(2, 51):
    is_prime = True
    for i in range(2, candidate):
        if candidate % i == 0:
            is_prime = False
            break
    if is_prime:
        print(candidate)