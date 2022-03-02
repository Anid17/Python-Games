#guess the number

import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input("Guess a number between 1 and {x} :"))
        print(guess)
        if guess < random_number:
            print("Sorry, too low ")
        elif guess > random_number:
            print("Sorry, too high ")
    print("You have guessed the number{random_number} correctly")

guess(10)



def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "C":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"is {guess} too high [H],too low[L] or correctly[C]")
        if feedback == "H":
            high = guess - 1
        elif feedback == "L":
            low= guess + 1
    print("The computer guessed your number correctly! ")

computer_guess(1000)
