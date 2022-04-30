# Create your own adventure with python here

def replay():
    return input('Do you want to play again? y or n').lower().startswith('y')

print('Welcome to Choose your Adventure!')
while True:
    play_game = input('Are you ready to play? y or n')
    if play_game.lower().startswith('y'):
        game_on = True
    else:
        print('Good Bye!')
        game_on = False
        break
    while game_on:
        choice1 = input('You are walking down a path and there is a fork in the road. Do you go left, right, pick it up or do nothing? l, r, p, n')
        if choice1.lower().startswith('l'):
            choice2 = input('You take the left path and stumble upon some bandits. Do you run or hide? r or h')
            if choice2.lower().startswith('h'):
                print('You try hiding, but an elephant comes out nowhere and squishes you. You died. The End')
                break
            else:
                print('You start running, you do some flips through the trees and amazing acrobatics. You eventually run into a dead end with the gang closing in.')
                print('They have you surrounded with nowhere to go. The leader comes up to you and says "Wow! you have amazing talents! Please join my circus troupe!"')
                print('You end up joining and living a good long life in circus. The End')
                break
        elif choice1.lower().startswith('r'):
            print('You come across a river. You see a brige far off in the distance, but the river looks shallow and and current looks slow.')
            choice3 = input('Do you go to the bridge to cross or do you try to swim across? b or s')
            if choice3.lower().startswith('s'):
                print('You begin to swim across, but you vastly underestimated the river and the current sweeps you down stream.')
                print('You are at the mercy of the river and you go over a waterfall. As you are falling, you think to yourself that this is the end.')
                print('Your lifeless body is dragged from the river, and with no recollection of who you are, you join the tribe that saved you. The End')
                break
            else:
                print('You start heading towards the bridge, but it takes days for you reach it.')
                print('you finally reach the bridge and stumble into town starving.')
                print('You see a vendor and start eating all his food. The vendor yells "HEY! QUIT EATING ALL MY FOOD!')
                print('With no money to pay the vendor, the guards haul you off to jail. Where you rot for the rest of your days. The End')
                break
        elif choice1.lower().startswith('p'):
            print('You pick up the fork. Smelling a slight hint of roast beef, you think to yourself, this is weird.')
            choice4 = input('You are walking along the path and stumble upon a pie eating contest. Do you join or keep walking? j or w')
            if choice4.lower().startswith('j'):
                print('With trusty fork in hand, you dig in. Unsure of victory, you keep eating.')
                print('All of a sudden, a loud voice booms "TIME IS UP!"')
                print('They declare you the winner! Feeling slightly nauseous, you walk away happy, full, and rich. The End')
                break
            else:
                print('You walk away from the contest, just minding your business when you hear a low growl behind you.')
                print('You look back and see a big hungry wolf looking at you. Fearing for your life, you turn and run.')
                print('As you are running, you trip, the fork flies out your hand and miraculously kills the wolf.')
                print('You retrieve your trusty fork, and look to see what made you stumble.')
                print('You see it is a partially buried chest. You open it and see it is full of gold!')
                print('You take you new found wealth into town and live and extravagant life. The End')
                break
        else:
            print('You are tired and sit on ground. Next thing you know, you start floating towards the sky.')
            print('Aliens have abducted you! After a long time of very invasive probing, they decide to take you to their home planet.')
            print('They put you in a zoo where you are on display for the rest of your life. The End')
            break
    if not replay():
        print('Thank you for playing!')
        break
