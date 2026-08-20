def safe_divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        print("Warning: Cannot divide by zero.")
        return None

    except TypeError:
        print("Warning: Invalid data type. Please use numbers.")
        return None

    finally:
        print("Operation attempted")


# Normal division
print(safe_divide(10, 2))

# Division by zero
print(safe_divide(10, 0))

# TypeError
print(safe_divide("10", 2))


# Operation attempted
# 5.0
# Warning: Cannot divide by zero.
# Operation attempted
# None
# Warning: Invalid data type. Please use numbers.
# Operation attempted
# None