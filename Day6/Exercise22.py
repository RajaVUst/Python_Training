
def try_read(path):
    try:
        with open(path) as f:
            f.read()
        print(f"Read {path} successfully")
    except FileNotFoundError:
        print(f"{path} was not found")
    finally:
        print("Attempt finished")

try_read("notes.txt")
try_read("ghost.txt")

#output
# Read notes.txt successfully
# Attempt finished

# ghost.txt was not found
# Attempt finished