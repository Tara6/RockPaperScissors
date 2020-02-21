def playerInfo():
    rounds = int(input("How many rounds do you want to play?: "))
    playerA = input("Please enter your name player A: ")
    playerB = input("Please enter your name player B: ")
    return rounds, playerA, playerB
    
def firstPlayerChoice(pa):
    print(pa, "has been chosen to start the game")
    print(pa, "please choose your weapon")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    firstplayerchoice = int(input("Enter your choice (without someone seeing): "))
    return firstplayerchoice

def secondPlayerChoice(pb):
    print(pb, "please choose your weapon")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    secondplayerchoice = int(input("Enter your choice (without someone seeing): "))
    return secondplayerchoice
