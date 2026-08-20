def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print(f"Warning: cannot divide {a} by zero.")
        return None
    except TypeError:
        print(f"Warning: unsupported types for division: {type(a).__name__} and {type(b).__name__}.")
        return None
    finally:
        print("Operation attempted.")

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("10", 2))
# Output:
# Operation attempted.
# 5.0
# Warning: cannot divide 10 by zero.
# Operation attempted.
# None
# Warning: unsupported types for division: str and int.
# Operation attempted.
# None