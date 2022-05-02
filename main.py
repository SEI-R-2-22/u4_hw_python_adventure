# Create your own adventure with python here
def play_word_game():

    print("Hello there! Welcome to the Accurate Typing Game!\n")
    print("Rules are simple, you must accurately type your responses in or you lose!\n")
    test = input(
        "Before we begin the, type in 'tEsTinG' (you must type each letter correctly between the apostrophes)\n")
    failure = "Well that's embarrassing, you failed!\n"

    if test == "tEsTinG":

        choices = input(
            "Type 'easy','mediUm', or 'HaRd' to play on a certain level difficulty\n")
        if choices == "easy":
            level_one = input(
                "Challenge: Type 'I think, therefore I am.' (Make sure to include the spaces!)\n")
            if level_one == "I think, therefore I am.":
                print(
                    "Congrats, you have beaten a level that even my grandma can beat, how does that make you feel?\n")
            else:
                print(failure)

        elif choices == "mediUm":
            level_two = input(
                "Challenge: Type 'AsPire to insPire before we exPire.' (Be careful of the 'P'!)\n")
            if level_two == "AsPire to insPire before we exPire.":
                level_two_part_2 = input(
                    "Challenge Part 2: Type 'And STILL, I RISE.' (Make NOTE of THE capital WORDS)\n")
                if level_two_part_2 == "And STILL, I RISE.":
                    print(
                        "You won! Don't feel so great though, you should feel accomplished when you beat the hard level...\n")
                else:
                    print(failure)
            else:
                print(failure)

        elif choices == "HaRd":
            level_three = input("Challenge: Type 'su'\n")
            if level_three == "su":
                level_three_part_2 = input("Challenge Part 2: Type 'per'\n")
                if level_three_part_2 == "per":
                    level_three_part_3 = input(
                        "Challenge Part 3: Type 'cAlIfrAgIlIstIcexpIAlIdocIous' (Let me remind you that this IS hard mode)\n")
                    if level_three_part_3 == "cAlIfrAgIlIstIcexpIAlIdocIous":
                        print(
                            "You won! Your Prize? The ability to say that you have beaten this game in hard mode!\n")
                    else:
                        print(
                            "You lost! I don't blame you, if there are winners, there will be losers >:)\n")
                else:
                    print(failure)
            else:
                print(failure)
        else:
            print("You didn't type it correctly!")
    else:
        print("You have failed! The game hasn't even started yet!!\n")


restart = 'Y'

while restart == 'Y':
    play_word_game()
    restart = input("Game end. Would you like to start over? Enter 'Y' for Yes or 'N' for No \n")

print("Hope you enjoyed the game! See you next time!")
