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


def int_check(question):


    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # check that number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main routine goes here

# intialise game variable

mode = "regular"
rounds_played = 1

print("🔼🔼🔼 Higher Lower Game 🔻🔻🔻")
print()

want_instructions = yes_no("Do you want to read instructions? ")

# checks users enter yes or no
if want_instructions == "yes":
    instruction()


# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like to play? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # round heading
    if mode == "infinite":
        rounds_heading = f"\n🙂🙂🙂 Round {rounds_played} (infinite Mode) 🙂🙂🙂"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1

    # if user choose infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1


