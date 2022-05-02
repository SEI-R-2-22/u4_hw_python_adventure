# Create your own adventure with python here
# from cmath import isnan
from math import*


gameover = False

while (not gameover):
    name = input('Please tell me your name.\n')

    if (len(name) > 5):
        print('Your name is very long. 😞\n')
        name = input('Perhaps make it less than 6 characters. Please choose a new name\n')
        if (len(name) > 5):
            print('you mock me with long names you have failed.\n')
            gameover = True
            #endpoint 1
        elif(not name[0].isupper()):
            print('Not enough dignity to capitalize your name. you have failed me')
            gameover = True
            # endpoint 2
        else:
            print('Very well ' + name + 'let\'s go')
    elif(not name[0].isupper()):
            print('Not enough dignity to capitalize your name. you have failed me')
            gameover = True
            # endpoint 3
    else:
        print('Very well ' + name + 'let\'s go')

    if(not gameover):
        age = input('Now that I know who you are '+ name +', how old are you?\n')

        if(int(age) == 1):
            print('Holy Moly! You must be a genius + 10 points')
        elif(int(age) > 21):
            print('Lets grab a drink')
        else:
            print('to young for some mead or you used letters or something!')

    play = input('Do you want to play a game?(y/n)')
    if (play == 'n'):
        print('then why are you here?')
        gameover = True
    else: print('I will take that as a yes')

    play = input('What game do you want to play?')

    if(play == 'catan' or 'Catan'):
        print ('one of my favorites!')
        print('you win!')
        gameover = True
    else: 
        print('I dont like that game')
        print ('you lose')
        gameover = True






    if(gameover):
        print(' 😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔')
        print(' 😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔')
        print(' 😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔')
        print(' 😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔')
        print('The game is over')
        print(' 😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔')
        print(' 😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔')
        print(' 😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔')

        playagain = input('Would you like to play again?(y/n)')
        if (playagain == 'y'):
            gameover= False