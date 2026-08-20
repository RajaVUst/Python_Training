Q1. Specific except (e.g. ZeroDivisionError) only catches that one failure
type; bare except: swallows everything — including bugs and
KeyboardInterrupt/SystemExit — hiding real problems.

Q2. finally always runs, success or failure — e.g. releasing a manually
opened DB connection back to a pool even if the query raised.

Q3. Catching FileNotFoundError/PermissionError/IsADirectoryError separately
lets the program react correctly to WHY it failed instead of showing one
vague generic message.