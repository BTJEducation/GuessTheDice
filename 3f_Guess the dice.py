# Guess the Dice
import random

spin_count=0
wins=0
users_guess=5

while users_guess>0:
    users_guess= int(input("Guess the roll of the dice (enter 0 to stop)"))

    number=random.randrange(1,7)
    spin_count = spin_count +1

    print("Number of spins {}.  The roll is: {} ".format(spin_count,number))

    if number==users_guess:
        wins += 1
        win_percent=wins/spin_count
        print("This is win number {}.  You win percentage is {:.2f}".format(wins,win_percent))
    else:
        print("You lose")

