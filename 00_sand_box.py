def check_rounds():
    while True:
        response = input("How many questions: ")
        round_error = "Please type either 1 " \
                      "or an integer that is more than 20"
        if response != "":
            try:
                response = int(response)
                if response > 20:
                    print(round_error)
                    continue
            except ValueError:
                print(round_error)
                continue
        return response


# Main routine goes here

rounds_played = 0
choose_instructions = "Please choose from  question (A) question (B) or question (C)"


# Ask user for # of rounds, <enter> for infinite mode

rounds = check_rounds()

end_game = "no"
while end_game == "no":
    # Start of Game Play Loop
    # Rounds Heading
    print()
    if rounds == "":
        heading = "continuous Mode:  "  "Round {}".format(rounds_played + 1)
    else:
        heading = "question {} of {}".format(rounds_played + 1, rounds)
    print(heading)
    choose = input("{} or 'xxx' to"
                   " end: ".format(choose_instructions))
    # end game if exit code is typed
    if choose == "xxx":
        break
    #  ***** rest of loop / game *****
    print("you choose {}".format(choose))

    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break
else:
    heading = "question {} of {}".format(rounds_played + 1, rounds)
    print(heading)
    choose = input(choose_instructions)
    # **** rest of loop / game ****
    print("you choose {}".format(choose))
    rounds_played += 1
    print("Thank you for playing")
