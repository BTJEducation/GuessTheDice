# Guess the Dice
import random

#----------------------------------------
def ask_user(prompt):
    ug=0
    while not(1 <= ug <=6):
        try:
            ug= int(input(prompt))
            if not (1 <= ug <= 6):
                raise ValueError()
        except ValueError:
            prompt="Invalid entry. It must be 1 to 6"
    return ug
#----------------------------------------
'''
Discussion: local variables.

prompt and ug are local to the function and their values are
not 'seen' outside of it
but values can be passed in and out of it.
ie. A message is passed in and the user's guess is out of it.

The string "Guess the roll of the dice" is passed into
the function and becomes prompt,
whilst ug is returned from the function and passes
the value to user_guess
'''
#----------------------------------------

spin_count=0
wins=0

while True:
    users_guess= ask_user("Guess the roll of the dice")  # see discussion on local variables above

    number=random.randrange(1,7)
    spin_count = spin_count +1

    print("Number of spins {}.  The roll is: {} ".format(spin_count,number))

    if number==users_guess:
        wins += 1
        win_percent=wins/spin_count
        print("This is win number {}.  You win percentage is {:.2f}".format(wins,win_percent))
    else:
        print("You lose")

