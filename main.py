import time
import random

# Create your own adventure with python here
def game():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Walking down the street you come to a fork in the road')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    time.sleep(3)
    print("One side of the road is dark and the other is light...")
    ch1 = str(input("Choose the dark path? [y/n]: "))
    if ch1 in ['y', 'Y', 'Yes', 'yes', 'YES']:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('A man in the dark hands you a note and says to read it')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        time.sleep(3)
        ch11 = str(input("Read the note? [y/n]: "))
        if ch11 in ['y', 'Y', 'Yes', 'yes', 'YES']:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('The note says.....')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            time.sleep(3)
            print("You should have choose the light...")
            time.sleep(1)
            print("BANG")
            time.sleep(2)
            print("GAME OVER YOU'RE TOAST")
            ch11end = str(input('Restart Game? [y/n]'))
            if ch11end in ['y', 'Y', 'Yes', 'yes', 'YES']:
                game()
        else: 
            print("You drop the note and run for your life...")
            time.sleep(3)
            print('~~~~~~~~ whew that was close.. ~~~~~~~~~~~~~~~~~')
            time.sleep(1)
            ch12 = str(input('Return home or go for a stroll in the park? [h/p]'))
            if ch12 in ['h', 'H', 'home', 'Home', 'HOME']:
                print("You safely walk inside your house...")
                time.sleep(2)
                print('As you walk down the hallway, you spot a trail of what looks like blood on the floor')
                time.sleep(1)
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                time.sleep(1)
                ch121 = str(input("Follow the trail? [y/n]"))
                if ch121 in ['y', 'Y', 'Yes', 'yes', 'YES']:
                    time.sleep(1)
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    time.sleep(1)
                    print('~~~~~~~~~~~~~ You run following the trail...~~~~~~~~~~')
                    time.sleep(2)
                    print("You come around the corner and in the open cabinet below the sink....")
                    time.sleep(2)
                    print("Is your neighbors kid your wife's babysitting with a bottle of ketchup")
                    ch121end = str(input('Restart Game? [y/n]'))
                    if ch121end in ['y', 'Y', 'Yes', 'yes', 'YES']:
                        game()
                else:
                    print("You decide to go to sleep waking up to realize everything was fine...")
                    ch122end = str(input('Restart Game? [y/n]'))
                    if ch122end in ['y', 'Y', 'Yes', 'yes', 'YES']:
                        game()
            else:
                print("As you walk into the park you see something shining in the grass...")
                ch111 = str(input("Walk over and pick it up? [y/n]"))
                if ch111 in ['y', 'Y', 'Yes', 'yes', 'YES']:
                    time.sleep(2)
                    print("Its a lock box...")
    else: print('death')
game()