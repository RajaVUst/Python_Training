def countdown(n):
    if n == 0:
        print("Liftoff!")
        return

    print(n)
    countdown(n - 1)

countdown(5)

#output

'''
5
4
3
2
1
Liftoff!
'''