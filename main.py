# Create your own adventure with python here

def start():
    print('')
    print('You wake up. You appear to be in a dark cave, only dimmly lit with torches. There are exits to the north, east and west.')
    direction = input('Which one do you take? (north, east, west, none)\n')

    if direction == 'north':
        print('')
        print('You walk to the room in the north.')
        print('In the center of the room there is a large wooden chest. Further along there is another exit.')
        choice1 = input('What do you do? Approch the chest? Or continue onward? (chest/continue)\n')
        if choice1 == 'chest':
            print('')
            print('You walk up to the chest, and open it. You go to pull your hands away and they wont pull away!')
            print('You realize it`s a mimic!')
            weapon = input('Do you attack it with your sword or do you use magic? (sword/magic)\n')
            if weapon == 'sword':
                print('')
                print('You go to reach for your sword, and you remember your hand is stuck to the mimic.')
                print('A large tongue comes out of the mimic and wraps around you, and pulls you inside itself')
                print('-')
                print('-')
                print('-')
                print('It`s dark and a little spongy inside the mimic. You quickly grow tired. It`s warm. You lay down.')
                replay = input('You hear a voice inside your head say, `Oh, you`ve been met with a terrible fate haven`t you? Do you wish to try again?` (yes/no)\n')
                if replay == 'yes':
                    start()
                else:
                    print('Goodnight...')
            elif weapon == 'magic':
                print('')
                print('You go to raise your hand to cast a fireball, and you remember your hand is stuck to the mimic.')
                print('A large tongue comes out of the mimic and wraps around you, and pulls you inside itself')
                print('-')
                print('-')
                print('-')
                print('It`s dark and a little spongy inside the mimic. You quickly grow tired. It`s warm. You lay down.')
                replay = input('You hear a voice inside your head say, `Oh, you`ve been met with a terrible fate haven`t you? Do you wish to try again?` (yes/no)\n')
                if replay == 'yes':
                    start()
                else:
                    print('Goodnight....')
        if choice1 == "continue":
            print('')
            print('You continue on to the next room.')
            print('You enter on to the next room.')
            print('It`s a room much like the last but without the chest. All you see is another exit')
            keep_going = input('Do you keep going? (yes/no)\n')
        
            if keep_going == 'yes':
                print('')
                print('You continue on to the next room.')
                print('You enter on to the next room.')
                print('It`s a room much like the last but without the chest. All you see is another exit')
                print('')
                print('Room after room all exactly the same.')
                print('You run for what feels like hours, maybe days.')
                print('Eventually you trip over your feet and tumble to a stop. Tears running down your face, you lay there accepting your fate.')
                print('You hear a voice in your head ')
                accept_defeat = input('`Oh, you`ve been met with a terrible fate haven`t you? Do you wish to try again?` (yes/no)\n')
                if accept_defeat == 'yes':
                    print('As you wish...')
                    start()
                else:
                    print('Goodnight....')
            elif keep_going == 'no':
                print('')
                print('You decide to lay down and take a nap')
                print('darkness envelopes you')
                print('You hear a voice in your head ')
                accept_defeat = input('`Oh, you`ve been met with a terrible fate haven`t you? Do you wish to try again?` (yes/no)\n')
                if accept_defeat == 'yes':
                    print('As you wish...')
                    start()
                else:
                    print('Goodnight....')

    if direction == 'east':
        print('')
        print('You decide to head to the exit to this east.')
        print('It`s a long hallway of sorts.')
        print('Eventually you find yourself approching a blinding bright light.')
        blinded_by_the_light = input('Do you approch the light? (yes/no)\n')
        
        if blinded_by_the_light == 'yes':
            print('')
            print('You start running towards the light.')
            print('It grows brighter and brighter the closer you get to it.')
            print('Eventually as you get ready to enter the source of the light it gets so bright you`re forced to close your eyes.')
            print('-')
            print('-')
            print('You hear what sounds like birds chirping.')
            print('Slowly you open your eyes')
            print('You appear to be outside! You turn around and see a familar looking cave enterance')
            print('As you admire your surrounding you hear a voice in your head say, ')
            print('"You`ve managed to escape, and so quickly too. Congratulations are in order. However... didn`t that seem too easy?"')
            once_more_with_feeling = input('"How about you give it another try?" (yes/no)\n')
            if once_more_with_feeling == 'yes':
                print('Excellent decison')
                print('')
                start()
            else:
                print('')
                print('Well that`s disappointing...')

        elif blinded_by_the_light == 'no':
            print('')
            print('Afraid of what the light could mean, and terrified of change, you start running back the way you came.')
            print('As you enter the threshold of the room where you began you trip over a large rock.')
            print('You smack your head very hard against the stone now below you')
            print('You slowly lose consciousness, and as you do, you start forgetting the adventure you were just on...')
            print('')
            start()

    if direction == 'west':
        print('')
        print('You decide the west is the direction for you, so you start for the western exit')
        print('As you enter the next, you see a skeleton wearing an emerald green cloak slumped against the far wall.')
        print('Obviously it`s not moving, it`s a skeletion.')
        print('What do you do? Approch the skeleton(it`s cloak looks very nice) or do you blast it with your magic, just to be safe?')
        skeletion = input('(approch/blast)\n')
        if skeletion == 'approch':
            print('')
            print('You approch the skeleton in the nice emerald cloak.')
            print('As you touch the clock to feel the material(it`s very nice btw) the skeleton wearing it crumbles away into dust')
            sketetion_dust = input('Well that was easy. Do you put on the cloak? (yes/no)\n')
            if sketetion_dust == 'no':
                print('')
                print('As you stay crouched there wondering what to do next, you accidentely breath in some of the bone dust left by the skeleton.')
                print('Suddenly it becomes very hard for you to breath.')
                print('You start coughing in hopes of expelling the bone dust from your system')
                print('Soon even that becomes difficult')
                print('The world around you begins to get hazy...')
                print('-')
                print('-')
                print('You die')
                print('-')
                print('-')
                print('-')
                print('-')
                try_again = input('Try again? (yes/no)\n')
                if try_again == 'yes':
                    print('Very well then')
                    start()
                else:
                    print("Goodnight...")
                    print('')
            if sketetion_dust == 'yes':
                print('')
                print('You put the cloak on, it seems to be a perfect fit on you.')
                print('It`s also a great color. You`ve always enjoyed the color green')
                print('Suddenly you hear a voice in your head say, ')
                print('"Excellent job, you were able to find my treasure, and were even stupid enough to put it on without examining it first!"')
                print('"It could have been cursed you know, but you meat head adventures never seem to think that far ahead."')
                print('"Thankfully for you, it`s not curse."')
                print('"The cloak will allow you to teleport out of the cave and to your safely... or of couse you could try your luck at one of the other rooms I planned so carefully for you"')
                is_it_time_to_leave_yet = input('Do you wish to stay and try again or leave? (stay/leave) \n')
                if is_it_time_to_leave_yet == 'leave':
                    print('')
                    print('The voice in you head seems to chuckle, "Yes thats probably for the best, goodnight..."')
                    print('-')
                    print('-')
                    print('You find yourself outside of a familar cave entrance.')
                    are_you_stupid = input('Do you enter the cave? (yes/no)\n')
                    if are_you_stupid == 'yes':
                        print('')
                        print('You enter the cave...')
                        print('It`s very dark inside')
                        print('The voice inside your head sighs')
                        print('You begin to lose consciousness, and you seem to feel the cloak leaving your body..')
                        print('')
                        start()
                    elif are_you_stupid == 'no':
                        print('')
                        print('You decide to leave the cave alone, something about it seems off.')
                        print('-')
                        print('Congrats!! You escaped the cave alive!!')
                elif is_it_time_to_leave_yet == 'stay':
                    print('')
                    print('The voice inside your head seems please when it says, "Ah yes, that is more fun, isnt it?"')
                    print('The world goes black around you.')
                    print('')
                    start()
        elif skeletion == 'blast':
            print('')
            print('Decideding that you don`t trust the look of sketeton, laying there, menancingly,')
            print('you raise your hand and shoot a fireball straight at it.')
            print('The skeleton crumbles to dust. The cloak it`s wearing burns to a crisp.')
            print('')
            print('A voice behind you says, "Well that was very rude wasn`t it?"')
            print('You spin around and see a giant skeleton approching you, wearing tattered armour and carrying a HUGE battleaxe')
            print('Uh-oh, you`re not sure how, but he looks angry.')
            skelly_battle = input('Do you, attack with your sword or do you blast it magic? (sword/magic)\n')
            if skelly_battle == 'sword':
                print('')
                print('You pull out your sword, and you deftly lunge at the skeleton with it.')
                print('...')
                print('Your sword goes through a couple of the skeletons ribs... you relaize you cant really stab a skeleton.')
                print('')
                print('The skeleton swings it`s axe down upon you, cleanly chopping off your neck')
                print('You have died...')
                youtube_rewind_time = input('Do you wish to try this adventure again? (yes/no)\n')
                if youtube_rewind_time == 'yes':
                    print('Very well...')
                    print('')
                    start()
                elif youtube_rewind_time == 'no':
                    print('Very well... goodnight...')
            elif skelly_battle == 'magic':
                print('')
                print('You raise your hand and start to charge up another fireball.')
                print('You go to shoot it at the skeleton and nothing but smoke leaves your hand.')
                print('...')
                print('Oh no!! You`ve used your magic too recently and it hasn`t rechanged yet!!')
                print('')
                print('The skeleton swings it`s axe down upon you, cleanly chopping off your neck')
                print('You have died...')
                youtube_rewind_time2 = input('Do you wish to try this adventure again? (yes/no)\n')
                if youtube_rewind_time2 == 'yes':
                    print('Very well...')
                    print('')
                    start()
                elif youtube_rewind_time2 == 'no':
                    print('Very well... goodnight...')

    elif direction == 'none':
        print('')
        print('Well you`re no fun, are you?')
        print('Choosing to do nothing when given 3 choices.')
        how_about_this_time = input('Do you want to make this choice again? (yes/no)\n')
        if how_about_this_time == 'yes':
            print('')
            print('Good. This time make a better decision.')
            print('')
            start()
        else:
            print('')
            print('Then why did you even come here?')
            print('')





start()