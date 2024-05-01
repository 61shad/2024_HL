
def int_check(question, low=None, high=None, exit_code=None):

    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"

    # if the numbers need to be more than an
    # integer (ie: rounds / 'high number')
    elif high is not None and low is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")

    # if the number needs to between low and high
    else:
        error = (f"Please enter an integer that is "
                 f"between {low} and {high} (inclusive)")
    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check if the integer is not too low...
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if the response is valid return it
            else:
                return response

        except ValueError:
            print(error)


# Guess Loop

# replace number below with random number between high / low values
secret = 7

# parameters that already exist in the base
low_num = 0
high_num = 10
guesses_allowed = 5

# set guesses used to zero at the start of each round
guesses_used = 0
already_guessed = []

guess = ""
while guess != secret and guesses_used < guesses_allowed:

    # ask the user the guess number...
    guess = int_check("Guess: ", low_num, high_num, "xxx")

    # check that they dont want to to quit
    if guess == "xxx":
        # set end-game to use so that outer loop can be broken
        end_game = "yes"
        break

    # check that guess is not a duplicate
    if guess in already_guessed:
        print(f"You have already guessed {guess}. You've *still* used."
              f"{guesses_used} / {guesses_allowed} guesses ")
        continue

    # if guess is not a duplicate, added it to the 'already guessed' list
    else:
        already_guessed.append(guess)

    guesses_used += 1

    # compare the user guess with the secret number set up feed back statement

    # if we have guesses left...
    if guess < secret and guesses_used < guesses_allowed:
        feedback = (f"Too low, please try a higher number. "
                    f"You've used {guesses_used} / {guesses_allowed} guesses")
    elif guess > secret and guesses_used < guesses_allowed:
        feedback = (f"Too high, please try a lower number. "
                    f"You've used {guesses_used} / {guesses_allowed} guesses")

    # when the secret number is guessed we have three different feedback
    # options (lucky / 'phew' / well done)
    elif guess == secret:

        if guesses_used == 1:
            feedback = " Lucky! You got it in the first guess. "
        elif guesses_used == guesses_allowed:
            feedback = f"Phew! You got it in {guesses_used} guesses."
        else:
            feedback = f"Well done! You guessed the secret number in {guesses_used} guesses."

    # if there are no guesses left...
    else:
        feedback = "Sorry - You have no more guesses. You lost this round. "

    # print feedback to user
    print(feedback)

    # Additional feedback ( warn the user that they are running out of guesses)
    if guesses_used == guesses_allowed - 1:
        print("\n Careful - you have one guess left.")

print()
print("End of round")