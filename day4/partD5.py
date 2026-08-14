num=int(input('Enter the number'))

def countdown(n):
    if n==0:
        print("Lift Off!")
        return
    
    print(n)
    countdown(n-1)

countdown(num)
        
# OUTPUT

# Enter the number5
# 5
# 4
# 3
# 2
# 1
# Lift Off!