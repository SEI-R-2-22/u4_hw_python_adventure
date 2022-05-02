# Create your own adventure with python here
def invalid():
    print('Please follow the prompts correctly')


def playAgain():
    answer = input("Type 'play' to play again ")
    if answer == 'play':
        playGame()


def playGame():
    print("Hi! You're planning on moving somewhere in the United States!")
    weather = input(
        "How are you with weather? Do you need to be in the sun? Answer 'yes' or 'no' ")
    if weather == 'yes':
        location = input('Would you like to move to the west or the south? ')
        if location == 'west':
            city = input(
                "Welcome to California! Would you like to go to the nation's tech capital or its entertainment capital? ")
            if city == 'tech':
                print('Welcome to San Francisco! Try not to get thrown in Alcatraz!')
                playAgain()
            elif city == 'entertainment':
                print(
                    "Welcome to Los Angeles! It's too bad the Lakers missed the playoffs, but you can still catch some waves!")
                playAgain()
            else:
                invalid()
                playAgain()
        elif location == 'south':
            city = input(
                "Welcome to the south. Are you just here for the weather or do you want really good barbeque? ")
            if city == 'weather':
                print('Welcome to Miami! Get a tan and catch a Heat game!')
                playAgain()
            elif city == 'barbeque':
                print("Welcome to Baton Rouge! Help yourself to the brisket! (I'm not from the South I really don't know where the best barbeque is)")
                playAgain()
            else:
                invalid()
                playAgain()
        else:
            invalid()
            playAgain()
    elif weather == 'no':
        location = input('Would you like to move to the east or the midwest? ')
        if location == 'east':
            print('Welcome to New York! Try not to get lost in the boroughs!')
            playAgain()
        elif location == 'midwest':
            city = input(
                'Welcome, try to get used to the cold! Are you a city person or a fishing person? ')
            if city == 'city':
                print(
                    'Welcome to Chicago! Help yourself to a deep dish pizza!')
                playAgain()
            elif city == 'fishing':
                print(
                    'Welcome to Duluth, Minnesota! Take a dip in Lake Superior!')
                playAgain()
            else:
                invalid()
                playAgain()
        else:
            invalid()
            playAgain()
    else:
        invalid()
        playAgain()


playGame()
