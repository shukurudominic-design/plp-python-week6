secret_number = 12
attempts = 0

while True:
    guess = int(input("Guess the secret number (1-20): "))
    attempts = attempts + 1

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Congratulations! You guessed it!")
        print(f"You got it in {attempts} tries!")
        break