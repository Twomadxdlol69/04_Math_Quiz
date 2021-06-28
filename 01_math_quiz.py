import random


# Functions go here
def check_rounds():
    while True:
        response = input("How many questions: ")
        round_error = "Please type a whole number between 1 / less than 20\n"
        if response != "":
            try:
                response = int(response)

                # if response is too low, go back to
                # start of loop
                if response > 20:
                    print(round_error)
                    continue
            except ValueError:
                print(round_error)
                continue
        return response

# Main routine goes here
questions_answered = 0
choose_instruction = "please choose answer question (A), question (B) or question (C)"

# ask user for # of questions between 1 and 20
question = check_rounds()

end_game = "no"
while end_game == "no":
    # Rounds Heading
    print()
    if question == "":
        heading = "continuous Mode: Round {}".format(questions_answered + 1)
    else:
        heading = "Question {} of {}".format(questions_answered + 1, question)
    print(heading)

    choose = input("{} or 'xxx' to end:".format(choose_instruction))

    if choose == 'xxx':
        break
    else:
        heading = "Question {} of {}".format(questions_answered + 1, question)
        print(heading)
        choose = input(choose_instruction)

    if questions_answered == question - 1:
        end_game = "yes"

        # rest of loop / game
        print("you choose {}".format(choose))
        questions_answered += 1
        print("Thank you for playing")

