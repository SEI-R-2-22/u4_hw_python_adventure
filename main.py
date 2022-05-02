# Create your own adventure with python here
from time import time


def game():
    print("welcome to Wilderness Survival")
    print("Where you make a series of choice to find out if you can get out alive")
    print("yes just like Bear Grylles.....Good Luck")
    str(input("would you like to play? [y/n]: "))
    if ('y','Y','Yes', 'YES', 'yes'):
        print("Aliright you have been dropped off in the middle of forest, somewhere in Canada")
        print("Now you have three choices")
        str(input("do you find make a fire, hunt for food, or find water? [fire/hunt/water]"))
        if ('fire', 'Fire', 'FIRE'):
            print("You wonder into the forest and find some wood to make a fire and shelter")
            print("the problem is that you need water and to find a way out of here")
            str(input("do you hike 2 miles up the mountain to gather snow for water or look for a stream [snow/stream]"))
            if ('snow','Snow', 'SNOW'):
                print('You climb up the mountain and you see a storm that is coming in quick.')
                print('you have no choice but to rush back to your shelter')
                print('you trigger an avalanche and die!')
                game()
            elif ('stream'):
                print('you make it down to the stream see that there is a trail and follow it to a road')
                print('someone finds you and you survive')
                game()
        elif ('hunt', 'Hunt', 'HUNT'):
            print("You set up some snare traps and catch a rabbit")
            print('you make a fire and eat but its getting dark out')
            str(input("do you make a shelter or get some food? [water/shelter]"))
            if ('water', 'Water', 'WATER'):
                print('You go find water but a storm moves in')
                print('You try to make a shelter but you are soaked and freeze to death!')
                game()
            elif ('shelter'):
                print('you make it back to your shelter eat your rabbit')
                print('you have found sernity in this experience and dicide to that you want to live this way')
                print('years past and everyone assumed you died')
                game()
        elif ('water', 'Water', 'WATER'):  
            print('You hike down to a river and you run into a grizzly bear')
            str(input("do you run, play dead, or try to scare it off [run/playdead/scare]"))
            if ('run'):
                print('bears a extremely fast and it chases you down and eats you!')
                game()
            elif('playdead'):
                print('You play dead and the bear does go away but does inspect you and steps on your legs and breaks them')
                game()
            elif('scare'):
                print('you put your back pack on your shoulders and jacket on a stick')
                print(' you get as big as possible and it scares the bear off')
                print('you follow the stream and you find a small town and have officially survided.')
                print('you are a pro at winderness survival')
                game()
    elif ('n', 'N', 'no', 'No', 'NO'):
        print("well fine I didnt want to play either")
        

game()