def countdown(n):
    if n < 1:           
        print("Liftoff!")
        return
    print(n)
    countdown(n - 1)     
 
countdown(5)

# Output:
# 5
# 4
# 3
# 2
# 1
# Liftoff!