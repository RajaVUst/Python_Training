
# ##  Specific exception vs bare except

# A specific exception catches only the type of error that we expect.

# For example:

#     except ZeroDivisionError:

# This handles only division-by-zero errors.

# A bare except:

#     except:

# catches almost every exception, including unexpected errors.

# A bare except is usually considered bad practice because it can hide
# unexpected bugs and make debugging difficult. It may also catch errors
# that the program should not silently handle.

# Therefore, it is better to catch specific exceptions whenever possible.






# ##  Purpose of finally

# The finally block is used for code that must execute whether an
# exception occurs or not.

# For example, if a program manually opens a file without using a
# with block, finally can be used to make sure the file is closed.

# Example real-world situation:

#     file = open("data.txt", "r")

#     try:
#         data = file.read()
#     finally:
#         file.close()

# Even if an error occurs while reading the file, the finally block
# will execute and close the file.

# This helps prevent resource leaks.





# ##  Why catch file exceptions separately?

# Python provides different exceptions for different file-related
# problems.

# For example:

# - FileNotFoundError → the requested file does not exist.
# - PermissionError → the program does not have permission to access
#   the file.
# - IsADirectoryError → a directory was provided where a file was
#   expected.

# Catching these separately is useful because each problem requires
# a different response.

# For example:

# - FileNotFoundError → ask the user to check whether the file exists.
# - PermissionError → ask for the correct permissions.
# - IsADirectoryError → check whether the correct file path was given.

# If we catch only a generic Exception, we lose this specific
# information and cannot provide an appropriate response.