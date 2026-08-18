with open("notes.txt","w") as f:
    f.write("AWS is the most used cloud platform\n")
    f.write("It has many data centers around the world\n")

with open("notes.txt","r") as f:
    print(f.readline().split())

# output

'''
AWS is the most used cloud platform
It has many data centers around the world
'''