secret_number = 3

guesses = [7, 0, 6, 3, 29]

for guess in guesses:

    if guess > secret_number:
        print(f"{guess}: Too high")

    elif guess < secret_number:
        print(f"{guess}: Too low")

    else:
        print(f"{guess}: Correct!")
        break