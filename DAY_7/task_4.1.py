def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Warning: division by zero — returning None")
        return None
    except TypeError:
        print(f"Warning: invalid types ({type(a).__name__}, {type(b).__name__}) — returning None")
        return None
    finally:
        print("Operation attempted")


print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("10", 2))
