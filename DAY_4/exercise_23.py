def build_utilities(operation, *values):
    if operation == "sum":
        return sum(values)
    elif operation == "max":
        return max(values)
    elif operation == "min":
        return min(values)
    elif operation == "average":
        return sum(values) / len(values)

print(build_utilities("sum", 4, 8, 15))        # Expected: 27
print(build_utilities("average", 2, 4, 6, 8))  # Expected: 5.0
print(build_utilities("max", 3, 7, 1, 9))      # Expected: 9
print(build_utilities("min", 3, 7, 1, 9))      # Expected: 1
