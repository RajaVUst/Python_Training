# input secret variable
secret_number = int(input("Enter a number: "))

# array of guesses
guesses = [10, 50, 35, 42, 60]

# loop through each guess in the array
for guess in guesses:
    if guess > secret_number:
        print(f"{guess}: Too high")
    elif guess < secret_number:
        print(f"{guess}: Too low")
    else:
        print(f"{guess}: Correct")
        break
