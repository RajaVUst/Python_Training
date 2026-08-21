def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Warning: Cannot divide by zero")
        return None
    except TypeError:
        print("Warning: Invalid data type")
        return None
    finally:
        print("Operation attempted")
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("10", 2))
print()
#  Output:
# Operation attempted
# 5.0
# Warning: Cannot divide by zero
# Operation attempted
# None
# Warning: Invalid data type
# Operation attempted
# None

