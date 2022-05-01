
def intro():
    name = input("what is your name?")
    start = input(
        'welcome to the game of tunnels would you like to play?(y/n)')
    if start == 'y':
        print('okay cool!')
    elif start == 'n':
        print('okay goodbye!')


intro()


def location():
    loc = input('you are underground and thre are 4 tunnels, pick 1-4 to begin')
    if loc == '1':
        restart = input(
            'oops, wrong choice, you have died would you like to start again? (y/n)')
        if restart == 'y':
            print('bye')
    elif loc == '2':
        b = input(
            'you have chose #2 good choice, you have survved another round(get up(y)(n))')
        if b == 'y':
            walking = input(
                'you find a path that leads into nothing but a dark hallway into a cave do you walk in it? (y/n)')
            if walking == 'y':
                print('you have a found a cave of spiders, you are now dead')

    elif loc == '3':
        c = input('option 3, you have fell into well')
    elif loc == '4':
        d = input(
            'tunnel 4 leads outside, you can run away (y) or keeep playing (n)')
        if d == 'y':
            print('goodbye')
        elif d == 'n':
            continu = input(
                'you have chose to continue, keep keep walking and hit a wall. (left or right?)')
            if continu == 'left':
                print('you have died!')
            elif continu == 'right':
                print(
                    'you wake up covered in roaches & rats with no way out & the cave fills with water')
        awake = input(
            '...hours go by... you think you are dead but you are not, you see a light, and you are now at a sandy beach! get up(y/n)')
        if awake == 'y':
            print(
                'you get picked up by an ambulance and make it to hospital. everything is ok and you recover. the end!')


location()
