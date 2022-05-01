# Create your own adventure with python here
from tkinter import dialog


def quest():
    player_name = input("Hello, adventurer! What is your name?")
    
    location = 'Nice to meet you %s, where would you like to go? There are 2 dungeons. Your choices are the islands (type 1) or the mountains (type 2).' %(player_name)
    
    islands_weapon = "I see you've chosen the tropics. Well I hope you're ready for all those sand mites, they can get nasty. It would probably be a good idea to arm yourself before going into the dungeon. Type 1 for sword, 2 for shield, or 3 for wand."
    islands_sword = "You pick up the sword and admire it's fine craft. How would you like to proceed? Type 1 to enter dungeon ready to fight. Type 2 to explore dungeon first. Type 3 for stealth mode."
    islands_sword_fight = "You fight your way through the dungeon and make it to the treasure room. Unfortunately you make so much noise that you have woken the dragon. You get burnt to a crisp and die. Type 'replay' to play again or 'end game' to exit."
    islands_sword_explore = "You get lost in the many tunnels and never find your way out. There are no monsters and no treasure, just endless black tunnels into nothingness. Type 'replay' to play again or 'end game' to exit."
    islands_sword_sneak = "You sneak your way through the dungeon and avoid battle. You survive but go home empty handed. Type 'replay' to play again or 'end game' to exit."
    islands_shield = "You lift the shield and feel it's weight. You are ready to enter the dungeon. Type 1 to enter with shield up and ready to defend, or type 2 for stealth mode."
    islands_shield_defend = "You enter the dungeon shield up and ready to defend, against what you are unsure. But what luck! The monsters of this dungeon are the 'keep to themselves' types and because you have no weapon they let you pass unhindered. You make your way through, take what treasure you like and...decide to stay. This place seems like a good one for a master of the shield. Type 'replay' to play again or 'end game' to exit."
    islands_shield_sneak = islands_sword_sneak
    islands_wand = "You grasp the wand and feel a tingling sensation flow through you. It's time to enter the dungeon. Type 1 to enter dungeon ready to fight. Type 2 to explore dungeon first. Type 3 for stealth mode."
    islands_wand_fight = "You enter the dungeon, it's pitch black, you can't see a thing. Then suddenly you feel something ooze down on you. Plop! A giant ball of slime envelopes you. You get absorbed into the slime immediately. Type 'replay' to play again or 'end game' to exit."
    islands_wand_explore = "You enter the dungeon and wander through its many tunnels. You find nothing and get bored. Rather than walk all the way back you simply teleport yourself home. Type 'replay' to play again or 'end game' to exit."
    islands_wand_sneak = "You carefully sneak through the dungeon but somehow you keep find your way out! No matter which direction you choose or how many times you enter the dungeon you keep winding up outside it. Finally you give up and go home empty handed. Type 'replay' to play again or 'end game' to exit."

    mountains_weapon = "I see you've chosen to traverse the mountainside. Well I hope you're ready for all those ornery goats, they can be quite aggressive this time of year. It would probably be a good idea to arm yourself before going into the dungeon. Type 1 for sword, 2 for shield, or 3 for wand."
    mountains_sword = "You pick up the sword and admire it's fine craft. How would you like to proceed? Type 1 to enter dungeon ready to fight. Type 2 to explore dungeon first. Type 3 for stealth mode."
    mountains_sword_fight = "You fight your way through the dungeon and make it to the treasure room. Unfortunately you make so much noise that you have woken the dragon. You get burnt to a crisp and die. Type 'replay' to play again or 'end game' to exit."
    mountains_sword_explore = "You get lost in the many tunnels and never find your way out. There are no monsters and no treasure, just endless black tunnels into nothingness. Type 'replay' to play again or 'end game' to exit."
    mountains_sword_sneak = "You sneak your way through the dungeon and avoid battle. You survive but go home empty handed. Type 'replay' to play again or 'end game' to exit."
    mountains_shield = "You lift the shield and feel it's weight. You are ready to enter the dungeon. Type 1 to enter with shield up and ready to defend, or type 2 for stealth mode."
    mountains_shield_defend = "You enter the dungeon shield up and ready to defend, against what you are unsure. But what luck! The monsters of this dungeon are the 'keep to themselves' types and because you have no weapon they let you pass unhindered. You make your way through, take what treasure you like and...decide to stay. This place seems like a good one for a master of the shield. Type 'replay' to play again or 'end game' to exit."
    mountains_shield_sneak = mountains_sword_sneak
    mountains_wand = "You grasp the wand and feel a tingling sensation flow through you. It's time to enter the dungeon. Type 1 to enter dungeon ready to fight. Type 2 to explore dungeon first. Type 3 for stealth mode."
    mountains_wand_fight = "You enter the dungeon, it's pitch black, you can't see a thing. Then suddenly you feel something ooze down on you. Plop! A giant ball of slime envelopes you. You get absorbed into the slime immediately. Type 'replay' to play again or 'end game' to exit."
    mountains_wand_explore = "You enter the dungeon and wander through its many tunnels. You find nothing and get bored. Rather than walk all the way back you simply teleport yourself home. Type 'replay' to play again or 'end game' to exit."
    mountains_wand_sneak = "You carefully sneak through the dungeon but somehow you keep find your way out! No matter which direction you choose or how many times you enter the dungeon you keep winding up outside it. Finally you give up and go home empty handed. Type 'replay' to play again or 'end game' to exit."


    choose_location = input(location)

# Islands -----------------------------------------------------------------

    if choose_location == '1':
        isl_choice1 = input(islands_weapon)

        if (isl_choice1 == '1'):
            sword_choice = input(islands_sword)

            if (sword_choice == '1'):
                last_choice = input(islands_sword_fight)
            elif (sword_choice == '2'):
                last_choice = input(islands_sword_explore)
            elif (sword_choice == '3'):
                last_choice = input(islands_sword_sneak)    

        elif (isl_choice1 == '2'):
            shield_choice = input(islands_shield)
            
            if (shield_choice == '1'):
                last_choice = input(islands_shield_defend)
            elif (shield_choice == '2'):
                last_choice = input(islands_shield_sneak)

        elif (isl_choice1 == '3'):
            wand_choice = input(islands_wand)

            if (wand_choice == '1'):
                last_choice = input(islands_wand_fight)
            elif (wand_choice == '2'):
                last_choice = input(islands_wand_explore)
            elif (wand_choice == '3'):
                last_choice = input(islands_wand_sneak)

# mountains -------------------------------------------------------------------

    if choose_location == '2':
        mnt_choice1 = input(mountains_weapon)

        if (mnt_choice1 == '1'):
            sword_choice = input(mountains_sword)

            if (sword_choice == '1'):
                last_choice = input(mountains_sword_fight)
            elif (sword_choice == '2'):
                last_choice = input(mountains_sword_explore)
            elif (sword_choice == '3'):
                last_choice = input(mountains_sword_sneak)    

        elif (mnt_choice1 == '2'):
            shield_choice = input(mountains_shield)
            
            if (shield_choice == '1'):
                last_choice = input(mountains_shield_defend)
            elif (shield_choice == '2'):
                last_choice = input(mountains_shield_sneak)

        elif (mnt_choice1 == '3'):
            wand_choice = input(mountains_wand)

            if (wand_choice == '1'):
                last_choice = input(mountains_wand_fight)
            elif (wand_choice == '2'):
                last_choice = input(mountains_wand_explore)
            elif (wand_choice == '3'):
                last_choice = input(mountains_wand_sneak)

# replay or end game ----------------------------------------------------------
    
    if (last_choice == 'replay'):
        quest()
    elif (last_choice == 'end game'):
        print("Game Over!")
        return 

quest()
