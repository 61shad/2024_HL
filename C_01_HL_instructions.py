# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeat if user don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


def instruction():
    print('''

*** Instructions ***
To begin, choose the number of the rounds and either customise
the game parameters or go with the default game (where the 
secret number will be between 1 and 100).

Then choose how many rounds do you want to play <enter> for 
infinite mode.

Your goal is to try to guess the secret number wihout 
running out of guesses. 

Good luck.
    ''')


# main routine goes here
print()
print("🔼🔼🔼 Higher Lower Game 🔻🔻🔻")
print()

# loop for testing purpose

want_instructions = yes_no("Do you want to read instructions? ")

# checks users enter yes or no
if want_instructions == "yes":
    instruction()

print("Program continues")