# Program that allows you to play rock paper or scissors against a robot
import random
playAgain = True

# functions for both sides choices
def yourChoice():
    global choice
    choice = str(input('Enter rock, paper, or scissors: '))

def computerChoice():
    global compChoice
    compChoice = random.choice(["rock", "paper", "scissors"])

# functions for win/loss message
def win():
    again = str(input("You won! Play again? (y/n) "))
    if again == "y":
        global playAgain
        playAgain = True
    else:
        playAgain = False

def lose():
    again = str(input("You lost! Play again? (y/n) "))
    if again == "y":
        global playAgain
        playAgain = True
    else:
        playAgain = False

def tie():
    again = str(input("You tied! Play again? (y/n) "))
    if again == "y":
        global playAgain
        playAgain = True
    else:
        playAgain = False

print("This program allows you to play rock paper scissors against a robot")

while playAgain == True:
    # have each side pick their choice
    yourChoice()
    computerChoice()

    # conditional logic
    if choice == compChoice:
        tie()
    elif choice == "rock" and compChoice == "scissors":
        win()
    elif choice == "paper" and compChoice == "rock":
        win()
    elif choice == "scissors" and compChoice == "paper":
        win()
    else:
        lose()





