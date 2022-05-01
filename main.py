# Create your own adventure with python here
from tkinter import dialog


def quest():
    player_name = input("Hello, adventurer! What is your name?")
    
    dialog2 = 'Nice to meet you %s, where would you like to go? There are 2 dungeons. Your choices are the islands (type 1) or the mountains (type 2).' %(player_name)
    dialog3 = "I see you've chosen the tropics. Well I hope you're ready for all those sand mites, they can get nasty. It would probably be a good idea to arm yourself before going into the dungeon. Type 1 for sword, 2 for shield, or 3 for wand."
    dialog4 = "You pick up the sword and admire it's fine craft. How would you like to proceed? Type 1 to enter dungeon ready to fight. Type 2 to explore dungeon first. Type 3 for stealth mode."
    dialog5 = "You fight your way through the dungeon and make it to the treasure room. Unfortunately you make so much noise that you have woken the dragon. You get burnt to a crisp and die. Type 'replay' to play again or 'end game' to exit."
    dialog6 = "You get lost in the many tunnels and never find your way out. There are no monsters and no treasure, just endless black tunnels into nothingness. Type 'replay' to play again or 'end game' to exit."
    dialog7 = "You sneak your way through the dungeon and avoid battle. You survive but go home empty handed. Type 'replay' to play again or 'end game' to exit."
    dialog8 = "You lift the shield and feel it's weight. You are ready to enter the dungeon. Type 1 to enter with shield up and ready to defend, or type 2 for stealth mode."
    dialog9 = "You grasp the wand and feel a tingling sensation flow through you. It's time to enter the dungeon. Type 1 to enter dungeon ready to fight. Type 2 to explore dungeon first. Type 3 for stealth mode."
    
    
    choose_location = input(dialog2)

    if choose_location == '1':
        isl_choice1 = input(dialog3)

    if (isl_choice1 == '1'):
        sword_choice = input(dialog4)

        if (sword_choice == '1'):
            sw_last_choice = input(dialog5)
        elif (sword_choice == '2'):
            sw_last_choice = input(dialog6)
        elif (sword_choice == '3'):
            sw_last_choice = input(dialog7)    

    elif (isl_choice1 == '2'):
        shield_choice = input(dialog8)

    elif (isl_choice1 == '3'):
        wand_choice = input(dialog9)
    
    
    if (sw_last_choice == 'replay'):
        quest()
    elif (sw_last_choice == 'end game'):
        print("Game Over!")
        return 

quest()
