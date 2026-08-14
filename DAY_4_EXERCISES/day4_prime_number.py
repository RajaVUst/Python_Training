def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def primes_up_to(limit):
    primes = []

    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)

    return primes

print(primes_up_to(30))

"""
Output ->
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
"""