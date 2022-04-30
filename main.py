# Create your own adventure with python here
def quest():


    player_name = input("Hello, adventurer! What is your name?")
    choose_location = input('Nice to meet you %s, where would you like to go? There are 2 dungeons. Your choices are the islands (type 1) or the mountains (type 2).' %(player_name))
    isl_choice = int(choose_location)
    if isl_choice == 1:
        islandsQ1 = input("I see you've chosen the tropics. Well I hope you're ready for all those sand mites, they can get nasty. It would probably be a good idea to arm yourself before going into the dungeon. Type 1 for sword, 2 for shield, or 3 for wand.")
        isl_choice1 = int(islandsQ1)
    if (isl_choice1 == 1):
        sword_choice = input("You pick up the sword and admire it's fine craft. How would you like to proceed? Type 1 to enter dungeon ready to fight. Type 2 to explore dungeon first. Type 3 for stealth mode.")
        if (sword_choice == 1):
            sw_last_choice1 = input("You fight your way through the dungeon and make it to the treasure room. Unfortunately you make so much noise that you have woken the dragon. You get burnt to a crisp and die. Type 'replay' to play again or 'end game' to exit.")
        elif (sword_choice == 2):
            sw_last_choice2 = input("You get lost in the many tunnels and never find your way out. There are no monsters and no treasure, just endless black tunnels into nothingness. Type 'replay' to play again or 'end game' to exit.")
        elif (sword_choice == 3):
            sw_last_choice3 = input("You sneak your way through the dungeon and avoid battle. You survive but go home empty handed. Type 'replay' to play again or 'end game' to exit.")    
    elif (isl_choice1 == 2):
        shield_choice = input("You lift the shield and feel it's weight. You are ready to enter the dungeon. Type 1 to enter with shield up and ready to defend, or type 2 for stealth mode.")
    elif (isl_choice1 == 3):
        wand_choice = input("You grasp the wand and feel a tingling sensation flow through you. It's time to enter the dungeon. Type 1 to enter dungeon ready to fight. Type 2 to explore dungeon first. Type 3 for stealth mode.")
    
    
    sw_last_choice1 = str(sw_last_choice1)
    sw_last_choice2 = str(sw_last_choice2)
    sw_last_choice3 = str(sw_last_choice3)
    if (sw_last_choice1 == 'replay' or sw_last_choice2 == 'replay' or sw_last_choice3 == 'replay'):
        quest()
    elif (sw_last_choice1 == 'end game' or sw_last_choice2 == 'end game' or sw_last_choice3 == 'end game'):
        return "Game Over"

quest()
