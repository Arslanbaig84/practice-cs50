import random
import sys

level = -1

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        continue

game = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0 and guess > game:
            print("Too large!")
            continue
        elif guess > 0 and guess < game:
            print("Too small!")
            continue
        elif guess > 0 and guess == game:
            print("Just right!")
            sys.exit(0)
        else:
            continue
    except ValueError:
        continue