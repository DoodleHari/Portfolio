import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)   # .choic it's a inbuilt method
    player = None

# for player in choices:    this line execute the code only 3 times the range is 3
    while player not in choices:    # while loop wil execute till the condtion gets false
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("computer: " + computer)
        print("player " + player)
        print("Tie")
    elif player == "rock":
        if computer == "scissors":
            print("computer: " + computer)
            print("player " + player)
            print("You Win")
        if computer == "paper":
            print("computer: " + computer)
            print("player " + player)
            print("You loss")

    elif player == "paper":
        if computer == "rock":
            print("computer: " + computer)
            print("player " + player)
            print("You Win")
        elif computer == "scissors":
            print("computer: " + computer)
            print("player " + player)
            print("You loss")

    elif player == "scissors":
        if computer == "paper":
            print("computer: " + computer)
            print("player " + player)
            print("You Win")
        elif computer == "rock":
            print("computer: " + computer)
            print("player " + player)
            print("You loss")

    playAgain = input("Play again? (y/n): ").lower()

    if playAgain != "y":
        break

print("bye bye")