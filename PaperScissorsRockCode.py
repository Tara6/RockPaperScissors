import random
playerBwins = 0
playerAwins = 0
roundcount = 0
print("Welcome to Rock, Paper, Scissors. In this game, You will verse one other willing player in the simple game of Rock paper scissors Python edition!")
rounds = int(input("How many rounds do you want to play?: "))
playerA = input("Please enter your name player A: ")
playerB = input("Please enter your name player B: ")

while roundcount < rounds:
    playerturn = random.randint(1, 2)
    if playerturn == 1:
       firstplayer = playerA
       secondplayer = playerB
    else:
        firstplayer = playerB
        secondplayer = playerA

    print(firstplayer, "has been chosen to start the game")
    print(firstplayer, "please choose your weapon")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    firstplayerchoice = int(input("Enter your choice (without someone seeing): "))

    if firstplayerchoice == 1:
        firstplayerweapon = "Rock"
    elif firstplayerchoice == 2:
        firstplayerweapon = "Paper"
    elif firstplayerchoice == 3:
        firstplayerweapon = "Scissors"
    else:
        firstplayerweapon = "Invalid choice"

    print(firstplayer, "chose", firstplayerweapon)

    print(secondplayer, "please choose your weapon")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    secondplayerchoice = int(input("Enter your choice (without someone seeing): "))

    if secondplayerchoice == 1:
        secondplayerweapon = "Rock"
    elif secondplayerchoice == 2:
        secondplayerweapon = "Paper"
    elif secondplayerchoice == 3:
        secondplayerweapon = "Scissors"
    else:
        secondplayerweapon = "Invalid choice"  

    print(secondplayer, "chose", secondplayerweapon) 

    print("Results:", firstplayer, "(",firstplayerweapon,")", "vs", secondplayer,"(", secondplayerweapon,")")

    if firstplayerchoice == 1 and secondplayerchoice == 3 or firstplayerchoice == 2 and secondplayerchoice == 1 or firstplayerchoice == 3 and secondplayerchoice == 2:
        print("Congratulations", firstplayer, "you've won the match!")
        if firstplayer == playerA:
         playerAwins = playerAwins + 1
        if firstplayer == playerB:
         playerBwins = playerBwins + 1
    elif firstplayerchoice == 1 and secondplayerchoice == 2 or firstplayerchoice == 2 and secondplayerchoice == 3 or firstplayerchoice == 3 and secondplayerchoice == 1:
        print("Congratulations", secondplayer, "you've won the match!")
        if secondplayer == playerA:
         playerAwins = playerAwins + 1
        if secondplayer == playerB:
         playerBwins = playerBwins + 1
    elif firstplayerchoice == 1 and secondplayerchoice == 1 or firstplayerchoice == 2 and secondplayerchoice == 2 or firstplayerchoice == 3 and secondplayerchoice == 3:
        print("Tie!")
    else:
        print("Invalid choice. Remeber to input a number between 1 and 3")
        roundcount -= 1
    print(playerA, "total wins: ", playerAwins)
    print(playerB, "total wins: ", playerBwins)
    roundcount += 1

print("Game Finished!")
if playerAwins > playerBwins:
    print(playerA, "wins!")
elif playerBwins > playerAwins:
    print(playerB, "wins!")
else:
    print("Tie game!")
print("Total Score:", playerA, "-", playerAwins, "|", playerB, "-", playerBwins)