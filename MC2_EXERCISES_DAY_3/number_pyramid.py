rows = 5
for i in range(1,5+1):
    for k in range(rows-i):
        print(" ", end=" ")
    for j in range(1,i*2):
        print(j, end=" ")
    print()