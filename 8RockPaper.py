import random

random = random.randint(1,9)

guess = 0
guessC = 0

while guess != random and guess != "exit":
    guess = input("enter your guess! ")
    guessC += 1

    if guess == "exit":
        break
    guess = int(guess)

    if guess > random:
        print("Lower")
    elif guess < random:
        print("Higher")
    else:
        print("correct",guessC,"tries")



