### 1. Specific exception vs bare except

Catching a specific exception, such as `ZeroDivisionError`, handles only the particular error we expect. This makes the program easier to understand and debug.

A bare `except:` catches almost any exception. It is usually considered bad practice because it can hide unexpected programming errors and make debugging more difficult.

### 2. Purpose of `finally`

The `finally` block contains code that should run whether an exception occurs or not.

For example, if a file is opened manually without using `with`, a `finally` block can close the file even if an error occurs while reading it. This ensures cleanup is performed.

### 3. Why catch file errors separately?

Different file exceptions describe different problems:

- `FileNotFoundError` means the file does not exist.
- `PermissionError` means the program does not have permission to access the file.
- `IsADirectoryError` means a directory was used where a file was expected.

Catching them separately is useful because the program can give a clear and appropriate message for each problem instead of treating every file error as the same generic error.