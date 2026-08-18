
def divide(a_str, b_str):
    try:
        a = int(a_str)
        b = int(b_str)
        result = a / b
    except ValueError:
        print("Please enter valid whole numbers.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"{a} / {b} = {result}")

divide("10", "2")
divide("10", "0")
divide("ten", "2")

#output
# 10 / 2 = 5.0
# Cannot divide by zero.
# Please enter valid whole numbers.