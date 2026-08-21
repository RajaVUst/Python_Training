"""
1. Catching a specific exception handles only the expected error,
   while a bare except catches every exception. Bare except is
   considered bad practice because it can hide unexpected bugs and
   make debugging difficult.

2. The finally block always executes whether an exception occurs
   or not. It is useful for cleanup tasks such as closing files,
   releasing resources, or disconnecting from a database.

3. Catching FileNotFoundError, PermissionError, and
   IsADirectoryError separately allows a program to respond
   appropriately to each problem. A generic Exception provides
   less information and makes troubleshooting harder.
"""