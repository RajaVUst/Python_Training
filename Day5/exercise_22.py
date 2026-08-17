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

# output
# {1: '1', 2: '2', 3: 'Fizz', 4: '4', 5: 'Buzz', 6: 'Fizz', 7: '7', 8: '8', 9: 'Fizz', 10: 'Buzz', 11: '11', 12: 'Fizz', 13: '13', 14: '14', 15: 'FizzBuzz', 16: '16', 17: '17', 18: 'Fizz', 19: '19', 20: 'Buzz'}{1: '1', 2: '2', 3: 'Fizz', 4: '4', 5: 'Buzz', 6: 'Fizz', 7: '7', 8: '8', 9: 'Fizz', 10: 'Buzz', 11: '11', 12: 'Fizz', 13: '13', 14: '14', 15: 'FizzBuzz', 16: '16', 17: '17', 18: 'Fizz', 19: '19', 20: 'Buzz'}