# Task 4.2 — Exception Handling: Concept Check
#
# Q1: Specific exception vs bare except:
#     A specific except clause (e.g., except ZeroDivisionError) only catches
#     that one error type, so unexpected errors still propagate and are visible.
#     A bare `except:` catches EVERYTHING — including SystemExit, KeyboardInterrupt,
#     and bugs you haven't thought of yet. This silently hides real problems and
#     makes debugging extremely hard. Best practice: always name what you expect.
#
# Q2: Purpose of finally:
#     The finally block runs no matter what happened in try/except — whether the
#     code succeeded, raised an exception, or even hit a return statement.
#     Real-world example: opening a database connection without `with`:
#
#       conn = db.connect()
#       try:
#           conn.execute(query)
#       except Exception as e:
#           log(e)
#       finally:
#           conn.close()   # always releases the connection, even if query fails
#
#     Without finally, an exception would leave the connection open indefinitely.
#
# Q3: Why catch FileNotFoundError / PermissionError / IsADirectoryError separately:
#     Each error means something different and requires a different response:
#       - FileNotFoundError  → tell the user the path is wrong, suggest checking the filename
#       - PermissionError    → the file exists but the process lacks rights; run as admin or fix ACLs
#       - IsADirectoryError  → the path points to a folder, not a file; the user may have a typo
#     Catching a single generic Exception collapses all three into one handler,
#     forcing you to re-examine the exception message to figure out what went wrong —
#     exactly the information that specific exception types already encode for free.

print("Concept check answers are in the comments above — no runnable output for this task.")
