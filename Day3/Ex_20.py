for i in range(2,51):
    if i%2==0:
        print(f"{i} is not a prime number")
        continue
    for j in range(3, int(i**0.5)+1, 2):
        if i%j==0:
            print(f"{i} is not a prime number")
            break
    else:
        print(f"{i} is a prime number")