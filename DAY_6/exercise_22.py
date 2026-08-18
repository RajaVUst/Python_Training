# Test 1: file exists
print("--- Test with existing file ---")
try:
    with open("notes.txt", "r") as f:
        content = f.read()
        print("File read successfully.")
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Attempt finished.")

# Test 2: file does not exist
print("\n--- Test with missing file ---")
try:
    with open("ghost.txt", "r") as f:
        content = f.read()
        print("File read successfully.")
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Attempt finished.")
