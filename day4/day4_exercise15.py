def countdown(n):
    if n == 0: # Base case
        print("Liftoff!")
        return
    
    print(n)
    countdown(n - 1)

countdown(5)

'''
OUTPUT:
5
4
3
2
1
Liftoff!
'''