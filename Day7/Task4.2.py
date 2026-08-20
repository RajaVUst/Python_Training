# 1. Specific exception versus bare except:
#
# A specific except block handles only an expected type of error.
# For example, except ZeroDivisionError handles division by zero.
#
# A bare except catches almost every error. This can hide unexpected
# programming mistakes and make debugging difficult. Therefore, catching
# specific exceptions is safer and clearer.


# 2. Purpose of finally:
#
# The finally block always executes whether an exception occurs or not.
#
# Example: If a database connection is opened manually, finally can close
# that connection even when the database operation fails.


# 3. Why catch file exceptions separately:
#
# FileNotFoundError means the requested file does not exist.
# PermissionError means the user cannot access the file.
# IsADirectoryError means a directory was supplied instead of a file.
#
# Catching them separately allows the program to show an accurate message
# and perform the correct recovery action for each problem.