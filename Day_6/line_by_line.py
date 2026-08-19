with open("notes.txt", "r") as f:
    for line in f:
        clean_line = line.strip()

        if not clean_line:
            continue

        print(clean_line.upper())

# output:
# HEY THERE
# I AM CHANDRASHEKHAR
# AND THIS IS THE 6TH DAY OF TRAINING