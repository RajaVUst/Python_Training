secret_number = 42
guesses = [10, 25, 42, 50]
for guess in guesses:
    if guess < secret_number:
        print(f"{guess}: Too low")
    elif guess > secret_number:
        print(f"{guess}: Too high")
    else:
        print(f"{guess}: Correct!")
        break
 