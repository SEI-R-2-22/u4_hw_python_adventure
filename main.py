# Create your own adventure with python here

# Endings
def first_ending():
    print("You turn around and leave Slide World through the door which you entered.  You feel as if you've made the right choice.")
    try_again = input("Try Again? (y / n) ")

    if try_again == "y":
        start_game()
    elif try_again == "n":
        print("Why don't you try again anyway?")
        start_game()
    else:
        first_ending()


def red_ending():
    print("You hop in the red slide and down you go.")
    print("As you whimsically slide down the plastic red tube, you hear load machinery")
    print("The machinery gets louder, until finally you pop out of the slide")
    print("into a room full of sharp, grinding machinery")
    print("You're ground up into a pink slime")
    try_again = input("Try Again? (y / n) ")

    if try_again == "y":
        start_game()
    elif try_again == "n":
        print("Why don't you try again anyway?")
        start_game()
    else:
        red_ending()


def blue_ending():
    print("You pull the plug and water begins to drain from the room.")
    print("You drained all the water!")
    print("You notice several fish (one has a little crown and robe)")
    print("dried up and flopping around on the floor.")
    print("You notice an exit high up in the room but you can't reach it.")
    print("After weeks of clawing at the walls and eating sentient fish to survive,")
    print("you run out of fish to eat...")
    print("You eventually die...")
    try_again = input("Try Again? (y / n) ")

    if try_again == "y":
        start_game()
    elif try_again == "n":
        print("Why don't you try again anyway?")
        start_game()
    else:
        blue_ending()


def blue_ending_alt():
    print("You decide not to hop in the green hole.")
    print('"Suit yourself" says the little fish king.')
    print('"Get him, boys!"')
    print("A bunch of tiny fish swim up to you and")
    print("begin eating your flesh.")
    print("Eventually, you become a skeleton.")
    print("Spooky.")
    try_again = input("Try Again? (y / n) ")

    if try_again == "y":
        start_game()
    elif try_again == "n":
        print("Why don't you try again anyway?")
        start_game()
    else:
        blue_ending_alt()


def yellow_ending():
    print("You lie down and rest your eyes for a bit.")
    print("You fall into a deep slumber.")
    print("Many years go by as you sleep.")
    print("Eventually, your body begins to become soft and plush.")
    print("You've turned into a pillow.")

    try_again = input("Try Again? (y / n) ")

    if try_again == "y":
        start_game()
    elif try_again == "n":
        print("Why don't you try again anyway?")
        start_game()
    else:
        yellow_ending()


def yellow_ending_alt():
    print('"Excellent my child!"')
    print('You walk up to the Goddess and embrace her')
    print('She hugs you, you fall asleep on her giant bossom.')
    print("You fall into a deep slumber.")
    print("Many years go by as you sleep.")
    print("Eventually, your body begins to become soft and plush.")
    print("You've turned into a pillow.")

    try_again = input("Try Again? (y / n) ")

    if try_again == "y":
        start_game()
    elif try_again == "n":
        print("Why don't you try again anyway?")
        start_game()
    else:
        yellow_ending_alt()


def green_ending():
    print("You slow your descent by pushing your arms into the ceiling of the tube.")
    print("You come to a stop.")
    print("You notice a flimsy point in the ceiling, and punch through it")
    print("You emerge out the hole you made and")
    print("realize you cannot breathe and everything is dark.")
    print("You're in  outer space")
    print("You float off into space, and freeze solid, preserving your body eternally.")
    print("eventually, you stop thinking.")

    try_again = input("Try Again? (y / n) ")

    if try_again == "y":
        start_game()
    elif try_again == "n":
        print("Why don't you try again anyway?")
        start_game()
    else:
        green_ending()
# Start Game


def start_game():
    print("Welcome to uhhhh.... Slide World! What's your name?")
    global name
    name = input("Enter your name: ")
    print(name + "... Cool Name! Do you want to pick a slide?")
    choice_one = input("Do you want to pick a slide? (y / n) ")

    if choice_one == "y":
        first_pick()
    elif choice_one == "n":
        first_ending()
    else:
        start_game()

# Round 1


def first_pick():
    first_slide = input(
        "In front of you are 3 plastic slide holes (Red, Blue, and Yellow).  Which one do you enter? (r / b / y) ")
    if first_slide == "r":
        red_ending()
    elif first_slide == "b":
        blue_slide()
    elif first_slide == "y":
        yellow_slide()
    else:
        first_pick()


def blue_slide():
    print("You hop in blue and down you go.")
    print("After a brief moment of sliding down a blue, plastic tube,")
    print("you emerge from the tube and splash down into a pool of water.")
    blue_slide_pick = input(
        '(s)wim to the bottom? (t)read water on top? (s / t) ')

    if blue_slide_pick == "s":
        blue_slide_s()
    elif blue_slide_pick == "t":
        blue_slide_t()
    else:
        blue_slide()


def yellow_slide():
    print("You hop in yellow and down you go.")
    print("After a brief moment of sliding down a yellow, plastic tube,")
    print("you emerge from the tube and land in a  pile of soft pillows.")
    print("You look around and are surrounded by vast, pillow society")
    print("After a brief moment of sliding down a yellow, plastic tube,")
    yellow_slide_pick = input("(s)tay put? (t)ry to find an exit? (s / t) ")

    if yellow_slide_pick == "s":
        yellow_slide_s()
    elif yellow_slide_pick == "t":
        yellow_slide_t()
    else:
        yellow_slide()

# Round 2


def blue_slide_s():
    print("You swim to the bottom and see a plug.")
    plug_pull = input("Pull the plug? (y / n) ")
    if plug_pull == "y":
        blue_ending()
    elif plug_pull == "n":
        print("You swim back to the top.")
        blue_slide_t()
    else:
        blue_slide_s()


def blue_slide_t():
    print("You tread water for a bit until suddenly you hear something...")
    print('"pssst... ' + name + '.... over here!"')
    print('You look and see a fish dressed like a little king.')
    print('"Hey dude, the exit is right here!"')
    print("The lil' fish king is pointing at a plastic green hole in the wall.")
    blue_pick = input("Jump in? (y / n) ")

    if blue_pick == "y":
        green_slide()
    elif blue_pick == "n":
        blue_ending_alt()
    else:
        blue_slide_t()


def yellow_slide_s():
    print("You stay put and realize how comfy the pillow ground is...")
    take_nap = input("Take a nap? (y / n) ")
    if take_nap == "y":
        yellow_ending()
    elif take_nap == "n":
        print("You decide to try and search for an exit after all")
        yellow_slide_t()
    else:
        yellow_slide_s()


def yellow_slide_t():
    print("After searching Pillow City for what felt like hours,")
    print('you reach a church. Inside is a giant, beautiful pillow goddess')
    print('"' + name + ', my child, do you seek an exit?"')
    print("If so, devote your life to me, the Pillow Goddess")
    yellow_pick = input("Devote life to Pillow Goddess? (y / n) ")

    if yellow_pick == "y":
        yellow_ending_alt()
    elif yellow_pick == "n":
        print("You produce a rock from your pocket and toss it at Pillow Goddess")
        print("She lets out a wail then fades to nothingness")
        print('You hear a voice cry out "How could you! You broke my illusion!"')
        print("Pillow city was just an illusion.")
        print("You see a green plastic hole in front of you and jump in.")
        green_slide()
    else:
        yellow_slide_t()

# Round 3


def green_slide():
    print("You hop in green and down you go.")
    print("After a brief moment of sliding down a green, plastic tube,")
    print("you realize it hasn't been a moment, its been hours.")
    print("You begin to panic.")
    last_choice = input("Stop sliding and jam yourself in the tube? (y / n) ")
    if last_choice == "y":
        green_ending()
    elif last_choice == "n":
        print("You keep sliding for another hour or two, and eventually ")
        print("you emerge into a bright room. ")
        start_game()
    else:
        green_slide()

# Run


start_game()
