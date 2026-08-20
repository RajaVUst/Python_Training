# Specific exception vs bare except

# A specific exception catches only the error we expect.
# Example:
# except ZeroDivisionError:
# A bare except catches almost every exception.
# Bare except is usually bad practice because it can hide unexpected errors
# and make debugging difficult.



# Purpose of Finally

# finally is used for code that must run whether an error occurs or not.
# For example, after working with a file, we may want to close the file
# even if an error occurs.



# Why catch different file errors separately?

# Different errors need different solutions.
# FileNotFoundError means the file does not exist.
# PermissionError means we do not have permission to access the file.
# IsADirectoryError means we tried to use a directory like a file.
# Handling them separately makes the error message clearer and helps us
# solve the correct problem.