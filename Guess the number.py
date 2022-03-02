import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input("Guess a number between 1 and {x} :"))
        print(guess)
        if guess < random_number:
            print("Too low, try again ")
        elif guess > random_number:
            print("Too high, try again ")

    print("You have guessed the number, congratulation")
guess(10)
