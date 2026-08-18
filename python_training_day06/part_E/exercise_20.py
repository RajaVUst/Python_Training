try:
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))

    result = first / second

    print(result)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")



#output:
'''Enter first number: 10
Enter second number: 2
5.0'''