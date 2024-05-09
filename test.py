import random

def guess_number_game():
    number_to_guess = random.randint(1, 100)
    low_guess = 1
    high_guess = 100
    guess = None
    while guess != number_to_guess:
        try:
            guess = int(input(f"Guess a number between {low_guess} and {high_guess}: "))
            if guess < low_guess or guess > high_guess:
                print(f"Please enter a number within the range {low_guess} and {high_guess}.")
            elif guess < number_to_guess:
                print("Higher.")
                low_guess = max(low_guess, guess + 1)
            elif guess > number_to_guess:
                print("Lower.")
                high_guess = min(high_guess, guess - 1)
        except ValueError:
            print("Please enter a valid integer.")

    print(f"Congratulations! You guessed the number {number_to_guess} correctly.")


