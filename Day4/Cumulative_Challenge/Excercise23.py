# Capstone 
def build_utilities(operation, *values):

    if operation == "sum":
        total = 0

        for value in values:
            total = total + value
        return total

    elif operation == "max":
        return max(values)

    elif operation == "min":
        return min(values)

    elif operation == "average":
        total = 0

        for value in values:
            total = total + value

        return total / len(values)
    else:
        return "Invalid operation"


print(build_utilities("sum", 4, 8, 15))
print(build_utilities("average", 2, 4, 6, 8))
print(build_utilities("min", 10,20,30))
print(build_utilities("max", 7,45,18))

# Output:
# 27
# 5.0
# 10
# 45