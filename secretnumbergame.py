# guess number game
# writing only from memory
import random

lowest = 0
highest = 30
max_guesses = 5
wins = 0
losses = 0


def score():
    return " (" + str(wins) + " wins. " + str(losses) + " losses.)"


while True:
    secret_number = random.randint(lowest, highest)
    attempt = 0
    print("Guess the number between " + str(lowest) + " and " + str(highest) + ":")

    while attempt < max_guesses:
        attempt += 1
        guess = int(input())
        if guess == secret_number:
            break
        elif guess < secret_number:
            print(
                "higher. "
                + str(max_guesses - attempt)
                + " guess"
                + ("" if max_guesses - attempt == 1 else "es")
                + " left"
            )
        elif guess > secret_number:
            print(
                "lower. "
                + str(max_guesses - attempt)
                + " guess"
                + ("" if max_guesses - attempt == 1 else "es")
                + " left"
            )
    if guess == secret_number:
        wins += 1
        print("Yep. tries: " + str(attempt) + score())
    else:
        losses += 1
        print("nope. it was actually " + str(secret_number) + score())
