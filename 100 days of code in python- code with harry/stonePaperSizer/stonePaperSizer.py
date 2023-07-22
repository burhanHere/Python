import random
import os
import platform

def comparison(a):
    if a == 'a':
        return "stone"
    elif a == 'b':
        return "paper"
    else:
        return "scissor"


def userInput():
    print("Select your move(a,b,c): a)stone b)paper c)scissors")
    while True:
        selection = input()
        if selection == 'a' or selection == 'b' or selection == 'c':
            return selection
        print("Invaid Input!!!!\nTry again: ")


def WinLoseCheck(a, b):
    if a==b:
        return "Game Tie"
    elif a=="stone":
        if b == "scissor":
            return "🎊🎉Congratulations You Won 🎊🎉"
        elif '''b == "paper"''':
            return "Unfortunately You Lost\nBetter Luck Next Time👍👍"
    elif a=="paper":
        if b == "scissor":
            return "Unfortunately You Lost\nBetter Luck Next Time👍👍"
        elif b == "stone":
            return "🎊🎉Congratulations You Won 🎊🎉"
    elif a=="scissor":
        if b == "stone":
            return "Unfortunately You Lost\nBetter Luck Next Time👍👍"
        elif b == "paper":
            return "🎊🎉Congratulations You Won 🎊🎉"
        
def game():
    playMore = bool(True)
    while playMore:
        if platform.system()=="Windows":
            os.system("cls")
        else:
            os.system("clear")            
        userSelection = userInput()
        userSelection = comparison(userSelection)
        botSelection = random.randint(97,99)
        botSelection = comparison(chr(botSelection))
        result = WinLoseCheck(userSelection, botSelection)
        print("Your selection: ",userSelection)
        print("Opinent selection: ",botSelection)
        print("____________________________")
        print(result.center(10))
        print("____________________________")
        print("Do you want to play again(y/n): ")
        while True:
            playMore = input()
            if playMore == 'y':
                playMore = True
                break
            elif playMore == 'n':
                playMore = False
                break
            print("Invalid input!!!\nTry again: ")


if __name__ == "__main__":
    game()
