# Create your own adventure with python here
def begin():
    print('Hello Brave Adventurer. Are you ready to play? (Yes/No) (press q at any time to quit)')
    response = input()
    game_state = False

    while response != 'q':
        if response == 'Yes':
            start_game()
        elif response ==  'No':
            print('Well, move along then. (press q to quit)')
        else:
            print('What was that? Please quit muttering. . . Yes or No? (press q to quit)')
        response = input()
def archer_play(player_class, weapon):
    game_state = True
    print("Ah, an archer, I should have guessed by the quiver and longbow! Well, a marauding group of goblins has raided our village. They burned the houses and stole all of the cattle from Old Man Jenkin's farm! They took the livestock back to their cave, but their leader stole away in the woods to wreak more havoc I'm sure. Tell me, can you help with our troubles? (1 - Rescue Cattle from the Cave. 2 - Hunt the Goblin Leader. 3 - Ignore this bumbling old man and go chase butterflies. It's your day off after all.")
    quest = input()
    while quest != 'q':
        if quest == '1':
            rescue_cattle(player_class, weapon)
        elif quest == '2':
            hunt_goblin(player_class, weapon)
        elif quest == '3':
            chase_butterflies(player_class, weapon)
        else:
            print('You really must speak up. What are you going to do? 1 - Rescue Cattle. 2 - Hunt Goblin Leader. 3 - Chase Butterflies')


def mage_play(player_class, weapon):
    game_state = True
    print("Ah, a mage, I should have guessed by your staff!  Well, a marauding group of goblins has raided our village. They burned the houses and stole all of the cattle from Old Man Jenkin's farm! They took the livestock back to their cave, but their leader stole away in the woods to wreak more havoc I'm sure. Tell me, can you help with our troubles? (1 - Rescue Cattle from the Cave. 2 - Hunt the Goblin Leader. 3 - Ignore this bumbling old man and go chase butterflies. It's your day off after all.")
    quest = input()
    while quest != 'q':
        if quest == '1':
            rescue_cattle(player_class, weapon)
        elif quest == '2':
            hunt_goblin(player_class, weapon)
        elif quest == '3':
            chase_butterflies(player_class, weapon)
        else:
            print('You really must speak up. What are you going to do? 1 - Rescue Cattle. 2 - Hunt Goblin Leader. 3 - Chase Butterflies')
 

def warrior_play(player_class, weapon):
    game_state = True
    print("Ah, a warrior, I should have guessed by the broadsword at your back!  Well, a marauding group of goblins has raided our village. They burned the houses and stole all of the cattle from Old Man Jenkin's farm! They took the livestock back to their cave, but their leader stole away in the woods to wreak more havoc I'm sure. Tell me, can you help with our troubles? (1 - Rescue Cattle from the Cave. 2 - Hunt the Goblin Leader. 3 - Ignore this bumbling old man and go chase butterflies. It's your day off after all.")
    quest = input()
    while quest != 'q':
        if quest == '1':
            rescue_cattle(player_class, weapon)
        elif quest == '2':
            hunt_goblin(player_class, weapon)
        elif quest == '3':
            chase_butterflies(player_class, weapon)
        else:
            print('You really must speak up. What are you going to do? 1 - Rescue Cattle. 2 - Hunt Goblin Leader. 3 - Chase Butterflies')

def rescue_cattle(player_class, weapon):
    print("You follow a path from the village to a great cave mouth. You hear drip of water and see dusted tracks of cattle hooves and goblin feet. You peer into the darkness. (1 - Draw your " + weapon +". 2 - sneak into the cave mouth. 3 - Call out")
    choice = input()
    while choice !='q':
        if choice == '1':
            print("You draw your " + weapon +  " and charge headfirst into the cave! An army of goblins bursts forth and surrounds you almost immediately. You try to fend them off but they mercilessly beat you to a pulp. Dang, that hurt to watch! (Play Again - Y / N ")
            res = input()
            while res != 'q':
                if res == 'Y':
                    begin()
                elif res == 'N':
                    quit()
                else:
                    print("Type 'Y' to continue or 'N' to quit")

        elif choice == '2':
            print("You sneak quietly into the mouth of the cave and lay your eyes upon a massive horde of goblins. You quickly deduce that you are indeed outnumbered, and the cows probably aren't worth it. You peace out, because honestly you don't get paid enough for this shit. Play Again? - Y / N ")
            res = input()
            while res != 'q':
                if res == 'Y':
                    begin()
                elif res == 'N':
                    quit()
                else:
                    print("Type 'Y' to continue or 'N' to quit")
        elif choice == '3':
            print("You call out and a cacophany of heckling goblin laughter echoes back at you. Scary stuff. You decide that it's probably best to leave it to some other professional. Like, what are you going to do with your rinky-dink " + weapon + "? Play Again? - Y / N ")
            res = input()
            while res != 'q':
                if res == 'Y':
                    begin()
                elif res == 'N':
                    quit()
                else:
                    print("Type 'Y' to continue or 'N' to quit")
    

def hunt_goblin(player_class, weapon):
    print("You follow tracks into the woods and come across a small sleeping troupe of goblins. They seem all worn out from burning and pillaging. What do you do? (1 - Leave them be. They look peaceful enough. 2 - MURDER THEM")
    choice = input()
    while choice !='q':
        if choice == '1':
            print("Hey, you're not a killer, that's cool. You let the beasts go. As you walk away you feel good. But then you think of all the lives those goblins probably ended today. And you don't feel so good. Man, the world is effed up. But hey, at least it's your day off. Play Again? - Y / N ")
            res = input()
            while res != 'q':
                if res == 'Y':
                    begin()
                elif res == 'N':
                    quit()
                else:
                    print("Type 'Y' to continue or 'N' to quit")    
        elif choice == '2':
            print("You take out your " + weapon + " and silently attack the goblins. It's brutal really. The blood. The stifled screams. I mean, who knows if these were even the same goblins. But you don't even care, do you? As long as you get to aimlessly run around killing anything you come across. You're sick. You're a sick man. But someone's gotta do it. Play Again? - Y / N ")
            res = input()
            while res != 'q':
                if res == 'Y':
                    begin()
                elif res == 'N':
                    quit()
                else:
                    print("Type 'Y' to continue or 'N' to quit")   
        else:
            print("That's not an option, bud. Type 1 or 2.")

def chase_butterflies(player_class, weapon):
    print("To hell with this old man and his tasks! You wander off into the forest giddily chasing butterflies. Just as you curl your fingers to retrieve a great monarch, you hear the snapping of twigs and the hiss of goblin tongue. 1 - You draw your " + weapon + ". 2 - You turn and run in the exact opposite direction of the sound.")
    choice = input()
    while choice !='q':
        if choice == '1':
            print('You turn to face your opponents head on. Good for you! Screw those gobbies. You run headlong into the fray with nary a care in the world. You dummy. You get clawed and beaten and kicked and scratched. You give some back though. You do good work and kill the enemies. But now you have to deal with infections of the wounds you sustained. In the medievel days. Have fun with bloodletting and leaches, sucka! Play Again? - Y / N ')
            res = input()
            while res != 'q':
                if res == 'Y':
                    begin()
                elif res == 'N':
                    quit()
                else:
                    print("Type 'Y' to continue or 'N' to quit")   
        elif choice == '2':
            print("You turn and run. You're a coward. It's good to be a coward - why does everyone come to you with their problems? Like you have any stake in it. Honestly these villagers should mind their own damn cows and maybe build some walls. Or a nice sturdy fence. How long has that cave been there? Didn't they notice it when they built the town? Anyway, you go on with your day because you're a champ. A big cowardly champ. Nice job. Play Again? - Y / N ")
            res = input()
            while res != 'q':
                if res == 'Y':
                    begin()
                elif res == 'N':
                    quit()
                else:
                    print("Type 'Y' to continue or 'N' to quit")   

        else:
            print("That's not an option, bud. Type 1 or 2.")

def start_game():
    game_state = True
    print("Okie doke. Let's start by telling me your name")
    name = input()
    print("Hello, " + name + " I'm glad fate guided us to cross paths at this dire hour. I see from your gear that you are strong and capable. Tell me, what is your class? (A- Archer, M - Mage, W - Warrior)")
    player_class = input()
    if player_class == 'A':
        chosen_class = 'Archer'
        weapon = 'longbow'
        archer_play(chosen_class, weapon)
    elif player_class == 'M':
        chosen_class = 'Mage'
        weapon = 'magic staff'
        mage_play(chosen_class, weapon)
    elif player_class == 'W':
        chosen_class = 'Warrior'
        weapon = 'broadsword'
        warrior_play(chosen_class, weapon)
    else:
        print("Hmm. Didn't catch that. What kind of fighter are you? (A- Archer, M - Mage, W - Warrior)")

begin()