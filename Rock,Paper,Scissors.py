import random

def play():
    user = input("(R) for Rock, (P) for Paper, (S) for scissors")
    computer = random.choice(["R","P","S"])

    if user == computer :
        return "Tie"

    if Win(user,computer):
        return "You won!"

    if Win(computer,user):
        return "You lost"

def  Win(player, opponent):
    if(player == "R" and opponent == "S") or (player == "S" and opponent == "P") or (player == "P" and opponent == "R"):
        return True

print(play())