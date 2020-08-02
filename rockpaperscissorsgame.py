# rock paper scissors game
# writing from memory only

import random

wins = 0
losses = 0
ties = 0

list = ["r", "p", "s"]
list_print = ["rock", "paper", "scissors"]


def compare(choice, enemy):
    global wins, losses, ties
    if choice == enemy:
        ties = ties + 1
        return "tie"
    elif (
        (choice == "r" and enemy == "s")
        or (choice == "p" and enemy == "r")
        or (choice == "s" and enemy == "p")
    ):
        wins = wins + 1
        return "win"
    else:
        losses = losses + 1
        return "loss"


while True:
    print("Choose (r)ock, (p)aper, or (s)cissors:")
    choice = input()
    if choice == "r" or choice == "p" or choice == "s":
        x = random.randint(0, 2)
        enemy = list[x]
        print(
            "The opponent chose "
            + list_print[x]
            + ". You "
            + compare(choice, enemy)
            + " ("
            + str(wins)
            + "-"
            + str(losses)
            + "-"
            + str(ties)
            + ")"
        )
