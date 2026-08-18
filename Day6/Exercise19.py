
test_value = "abc"
try:
    number = int(test_value)
except ValueError:
    print(f"'{test_value}' is not a valid number.")
    
#output
# 'abc' is not a valid number.