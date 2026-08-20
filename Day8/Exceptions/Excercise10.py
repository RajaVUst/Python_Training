def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None

    except TypeError:
        print("Please enter numbers")
        return None
    finally:
        print("Operation attempted")


print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("10", 2))

# Output:
# Operation attempted
# 5.0
# Cannot divide by zero
# Operation attempted
# None
# Please enter numbers
# Operation attempted
# None