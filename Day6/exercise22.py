# Day 6 - Exercise 22

def risky_file_read(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())

    except FileNotFoundError:
        print(f"{filename} was not found.")

    finally:
        print("Attempt finished")


risky_file_read("notes.txt")
risky_file_read("ghost.txt")