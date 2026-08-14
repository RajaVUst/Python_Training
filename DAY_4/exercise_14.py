# Lambda version
cube = lambda x: x ** 3

print(cube(3))  # Expected: 27

# Equivalent regular function
def cube_func(x):
    return x ** 3

print(cube_func(3))  # Expected: 27

# Comparison:
# Both produce the same result. The lambda is a compact single-expression form,
# useful for short, throwaway functions. The def version is more readable and
# supports multi-line logic, docstrings, and better debugging (has a proper name).
