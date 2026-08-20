def safe_divide(a, b):
    try:
        return a / b
 
    except ZeroDivisionError:
        print("Warning: Cannot divide by zero.")
        return None
 
    except TypeError:
        print("Warning: Invalid data type provided.")
        return None
 
    finally:
        print("Operation attempted")
 
 
# Examples
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("10", 2))
 