secret = 56
numbers = [1,4,6,9,16,44,53,56,68,70]

for i in numbers:
    if i<secret:
        print("Too low")
    elif i>secret:
        print("Too High")
    else:
        print("Correct")
        break