# Create your own adventure with python here
# door1=['left','right']
# door2=['left','right']
# door3=['left','right']
# door4=['left','right']






def adventure():
    print('Escape the haunted mansion')

    path1 = input('Which door do you go through? one, two, three, or four?:  ')
    
    if path1 == 'one':
            print('you have entered the bedroom!')
            decision1 = input('The door closes behind you! Do you hide or jump out the window? (hide/jump):  ')

            if decision1 == 'hide':
                print('you have chosen to hide under the bed and you hear foot steps near by')
                hide1 = input('do you attack the person or do you follow behind him?(follow/attack): ')
                if hide1 == 'attack':
                    print('its a ghost. He posses you. Its over')
                    decision4 = input('would you like to try again? (y/n):  ')
                    if decision4 == 'y':
                        adventure()
                    elif decision4 == 'n':
                        print('Boooo ur lame')
                else:
                    print('you follow him outside and escape!')
            else:
                print('you fall to your death...great job')
                decision4 = input('would you like to try again? (y/n):  ')
                if decision4 == 'y':
                    adventure()
                elif decision4 == 'n':
                    print('Boooo ur lame')


    elif path1 == 'two':
            print('you have entered the dining room! Find something to defend youself with! ')
            decision2 = input('knife or flashlight: ')
            print('what next? Should you enter the living room or try to open the back door?')
            decision3 = input('living room or back door: ')


            if decision3 == 'living room':
                print('A Ghost is chasing you!')
                if decision2 == 'knife':
                    print('you tried to stab it and got possessed. You lose.')
                    decision4 = input('would you like to try again? (y/n):  ')

                    if decision4 == 'y':
                        adventure()

                    elif decision4 == 'n':
                        print('Boooo ur lame')


                if decision2 == 'flashlight':
                    print('your flashlight scared him away! The doors open up! RUN. YOU ARE FREE')

            else:
                if decision2 == 'knife':
                    print('the door was locked and you tried to pry it open with your knife but it bent')
                    print('A Ghost is chasing you!')
                    print('you tried to stab it and got possessed. You lose.')
                    decision4 = input('would you like to try again? (y/n):  ')
                    if decision4 == 'y':
                        adventure()
                    elif decision4 == 'n':
                        print('Boooo ur lame')
                if decision2 == 'flashlight':
                    print('your flashlight scared him away!')
    elif path1 == 'three':
        print('You walk into a room with a casket and an open grave')
        print('you hear something coming')
        decision5 = input('do you hide in the grave or the casket?: ')
        if decision5 == 'grave':
            print('The ghost finds you and burries you alive !')
            decision4 = input('would you like to try again? (y/n):  ')
            if decision4 == 'y':
                adventure()
            elif decision4 == 'n':
                print('Boooo ur lame')
        else:
            print('the ghost comes in but can not find you. It leaves')
            print('you do another look around and find a trap door that leads outside. YOU ARE FREE')
    else:
        print('you find a room with a demon')
        demon_choice=input('he offers you a deal...he will grant you freedom from the mansion, but he keeps your soul. Do you take it (y/n)?: ')
        if demon_choice == 'y':
            print('you are free, but without your soul life feels meaningless')
        else:
            print('you are stuck in the house till death')

adventure()