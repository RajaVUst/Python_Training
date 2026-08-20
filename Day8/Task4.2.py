#1.Specific exception vs bare except
# Catching a specific exception means we handle only the error we expect.
# Example:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

# A bare except catches almost every exception:
# try:
#     ...
# except:
#     ...
# Bare except is usually bad practice because it can hide unexpected
# programming errors and make debugging difficult.

#2. Purpose of finally
# finally runs whether an exception occurs or not.
# It is useful for cleanup operations.
# Example:
# A database connection should be closed after the operation,
# even if an error occurs.
# with open(...) is normally preferred for files, but finally can be
# useful when manually managing resources.

#3 Why catch different file exceptions separately?

# Different exceptions represent different problems:
# FileNotFoundError:
#     The requested file does not exist.
# PermissionError:
#  The program does not have permission to access the file.
# IsADirectoryError:
#A directory was supplied where a file was expected.
# Handling them separately allows the program to give a more useful
# error message and take an appropriate action.