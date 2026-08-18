with open("notes.txt", "r") as source:
    with open("notes_upper.txt", "w") as destination:
        for line in source:
            destination.write(line.upper())

with open("notes_upper.txt", "r") as f:
    print(f.read())

#Output

'''
AWS IS THE MOST USED CLOUD PLATFORM
IT HAS MANY DATA CENTERS AROUND THE WORLD
TODAY I LEARNT ABOUT EC2 AND S3 BUCKETS

'''