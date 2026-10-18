"""Guess a random number from 1 to 100."""

import random


def main():
    secret = random.randint(1, 100)
    attempts = 0
    print("I picked a number from 1 to 100.")
    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Enter a whole number.")
            continue
        attempts += 1
        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"Correct! You needed {attempts} attempts.")
            break


if __name__ == "__main__":
    main()
