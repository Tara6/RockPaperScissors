import playerInformation
import random
playerBwins = 0
playerAwins = 0
roundcount = 0

def firstPlayerWeapon(weaponA):
  if weaponA == 1:
        firstplayerweapon = "Rock"
        return firstplayerweapon
  elif weaponA == 2:
        firstplayerweapon = "Paper"
        return firstplayerweapon
  elif weaponA == 3:
        firstplayerweapon = "Scissors"
        return firstplayerweapon
  else:
        firstplayerweapon = "Invalid choice"
        return firstplayerweapon

def secondPlayerWeapon(weaponB):
  if weaponB == 1:
        secondplayerweapon = "Rock"
        return secondplayerweapon
  elif weaponB == 2:
        secondplayerweapon = "Paper"
        return secondplayerweapon
  elif weaponB == 3:
        secondplayerweapon = "Scissors"
        return secondplayerweapon
  else:
        secondplayerweapon = "Invalid choice"
        return secondplayerweapon

print("Welcome to Rock, Paper, Scissors. In this game, You will verse one other willing player in the simple game of Rock paper scissors Python edition!")
rounds, playerA, playerB = playerInformation.playerInfo()

while roundcount < rounds:
    playerturn = random.randint(1, 2)
    if playerturn == 1:
       firstplayer = playerA
       secondplayer = playerB
    else:
        firstplayer = playerB
        secondplayer = playerA

    firstplayerchoice = playerInformation.firstPlayerChoice(firstplayer)
    secondplayerchoice = playerInformation.secondPlayerChoice(secondplayer)

    print("Results:", firstplayer, "(",firstPlayerWeapon(firstplayerchoice),")", "vs", secondplayer,"(", secondPlayerWeapon(secondplayerchoice),")")

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







