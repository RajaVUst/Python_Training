"""1. Difference Between Specific Exception and Bare except:
 
A specific exception handler catches only the expected error.
 
Example:
except ZeroDivisionError:
 
This handles only division-by-zero errors.
 
A bare exception handler:
 
except:
 
catches every exception, including unexpected ones such as KeyboardInterrupt and SystemExit.
 
Why is bare except bad practice?
- It can hide real bugs.
- Makes debugging difficult.
- May accidentally catch system-level exceptions.
- Makes code harder to maintain and understand.
 
Therefore, catching specific exceptions is safer and more readable.
 
 
2. Purpose of finally:
 
The finally block runs whether an exception occurs or not.
 
It is mainly used for cleanup operations that must always happen.
 
Example:
If a file is opened manually using open(), it should be closed in finally so that the file handle is released even if an error occurs while reading or writing.
 
Other examples:
- Closing database connections
- Releasing locks
- Closing network sockets
- Cleaning temporary resources
 
 
3. Why Catch File Exceptions Separately?
 
Different exceptions represent different problems:
 
- FileNotFoundError → File does not exist.
- PermissionError → Access is denied.
- IsADirectoryError → A directory was provided instead of a file.
 
Catching them separately allows the program to provide accurate error messages and take different corrective actions.
 
Example:
A missing file may require creating the file, while a permission error may require changing permissions.
 
This improves debugging, user experience, and maintainability."""
 