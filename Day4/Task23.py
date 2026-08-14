def build_utilities(operation, *values):
    if operation == "sum":
        return sum(values)
    elif operation == "max":
        return max(values)
    elif operation == "min":
        return min(values)
    elif operation == "average":
        return sum(values) / len(values)
    else:
        return "Invalid operation"
 
 
print(build_utilities("sum", 4, 8, 15))
print(build_utilities("average", 2, 4, 6, 8))
print(build_utilities("max", 10, 25, 3, 17))
print(build_utilities("min", 10, 25, 3, 17))
 
#Output:
"""
27
5.0
25
3
"""
 