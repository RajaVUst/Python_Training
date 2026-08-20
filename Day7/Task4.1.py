def safe_divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        print("Warning: division by zero is not allowed.")
        return None

    except TypeError:
        print("Warning: both values must be numbers.")
        return None

    finally:
        print("Operation attempted")


print("Result:", safe_divide(10, 2))
print("Result:", safe_divide(10, 0))
print("Result:", safe_divide("10", 2))

#output
'''
Operation attempted
Result: 5.0
Warning: division by zero is not allowed.
Operation attempted
Result: None
Warning: both values must be numbers.
Operation attempted
Result: None
'''