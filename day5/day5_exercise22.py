def fizzbuzz_map(n):
    result = {}

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result[i] = "FizzBuzz"
        elif i % 3 == 0:
            result[i] = "Fizz"
        elif i % 5 == 0:
            result[i] = "Buzz"
        else:
            result[i] = str(i)

    return result


print(fizzbuzz_map(20))