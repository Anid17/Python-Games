print(" Welcome to the quiz!! ")

playing = input("Do you wanna start the game? ")
score = 0
if playing != "yes":
    quit()

print("Let's play ")

answer = input("What does CPU stand for? " )

if answer == "center processing unit" :
    print("Congratulations, you got the right answer. ")
    score += 1
    print("Your score is : " + str(score))
else:
    print ("False")


