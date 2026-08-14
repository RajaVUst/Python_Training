rows = 5

for i in range(1,5+1):
    for k in range(rows-i):
        print(" ", end=" ")
    for j in range(1,i*2):
        print(j, end=" ")
    print()

"""
Output ->
        1 
      1 2 3 
    1 2 3 4 5 
  1 2 3 4 5 6 7 
1 2 3 4 5 6 7 8 9 
"""