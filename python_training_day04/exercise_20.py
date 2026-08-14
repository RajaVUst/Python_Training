def fizzbuzz_range(start, end):
    for i in range(start, end + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz_range(1, 20)


#output:
'''1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
Buzz
Fizz
16
17
Fizz
19
Buzz'''