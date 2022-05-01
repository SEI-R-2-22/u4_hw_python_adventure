# Create your own adventure with python here
def game():
    setAnswer = False
    answer = ''
    print('You are off on an adventure! You pack your things and head towards the edge of the village. You see 2 paths in front of you. Where do you go? (A/B)')
    print('a. Forrest')
    print('b. Mountains')

    while not setAnswer:
        answer = input('Answer: ')
        if answer.lower() == 'a' or answer.lower() == 'b':
            setAnswer = True

    if answer.lower() == 'a':
        setAnswer = False
        print('As you journey through the forrest, you start to hear whispers in front of you. You think to yourself: (A/B)')
        print('a. Do I Press on?')
        print('b. Do I Turn back?')

        while not setAnswer:
            answer = input('Answer: ')
            if answer.lower() == 'a' or answer.lower() == 'b':
                setAnswer = True 

        if answer.lower() == 'a':
            setAnswer = False
            print('You carry on. Nothing is going to stop you. Suddenly, out of nowhere, you spot a troll. As you back away you step on a branch and catch his attention. Do you ....? (A/B/C)')
            print('a. run?')
            print('b. stand your ground?')
            print('c. ummmm.......')

            while not setAnswer:
                answer = input('Answer: ')
                if answer.lower() == 'a'  or answer.lower() == 'b' or answer.lower() == 'c':
                    setAnswer = True 

            if answer.lower() == 'a':
                print("The troll laugh's at you as you coward away.")
            elif answer.lower() == 'b':
                print("You realize you have no weapons. You gather your courage and start running towards him, screaming at the top of your longs. The troll, never having heard such a scream, panics and flees. You realize you are safe for now.")
            elif answer.lower() == 'c':
                print("The troll rushes toward you and as he reaches out to grab you, you blackout.")

        elif answer.lower() == 'b':
            setAnswer = False
            print("You get cold feet. You think you're not ready yet. Do you ...? (A/B)")
            print('a. head back home?')
            print('b. hype yourself up?')

            while not setAnswer:
                answer = input('Answer: ')
                if answer.lower() == 'a':
                    setAnswer = True

            if answer.lower() == 'a':
                print("You open your door and wonder what happened? Was I not ready? did I forget somehting? We'll try again tomorrow.")
            elif answer.lower() == 'b':
                print('After pumping yourself up, you finally decide to pick a path.')

    elif answer.lower() == 'b':
        setAnswer = False
        print("You're walking down the mountain path and a cloud of fog decends upon you. You start seeing shadows move in front of you. You think to yourself: (A/B)")
        print('a. Like that is going to stop me.')
        print('b. Do I Turn back?')

        while not setAnswer:
            answer = input('Answer: ')
            if answer.lower() == 'a' or answer.lower() == 'b':
                setAnswer = True

        if answer.lower() == 'a':
            setAnswer = False
            print('You start hearing whispers. "If you dare continue, beware of what you see." (A/B/C)')
            print('a. Light your torch.')
            print('b. Close your eyes.')
            print('c. Track down the whispers.')

            while not setAnswer:
                answer = input('Answer: ')
                if answer.lower() == 'a' or answer.lower() == 'b' or answer.lower() == 'c':
                    setAnswer = True

            if answer.lower() == 'a' or answer.lower() in 'light your torch.':
                print("You grab a match and light a spark. It wasn't until the you saw the spark turn green that you knew this was a mistake. BOOOOOM!!!")

            if answer.lower() == 'b' or  answer.lower() in 'close your eyes.':
                print("You take the advice of the whispers and decide to close your eyes. You start to move foward and can feel the fog dissapear. You open your eyes and realize you've made it past the mountain path. You can't beleive what just happen and this is only the beginning.")

            if answer.lower() == 'c' or answer.lower() in 'track down the whispers.':
                print('"Who are you! Where are you!" You start tracking down the voice. after twist and turns you no longer know where you are. You have lost the path. Will you ever get out of the mountain? No one but you will know the answer.')
            
        elif answer.lower() == 'b':
            setAnswer = False
            print("You get cold feet. You think you're not ready yet. Do you ...? (A/B)")
            print('a. head back home?')
            print('b. hype yourself up?')

            while not setAnswer:
                answer = input('Answer: ')
                if answer.lower() == 'a' or answer.lower() == 'b':
                    setAnswer = True

            if answer.lower() == 'a':
                print("You open your door and wonder what happened? Was I not ready? did I forget somehting? We'll try again tomorrow.")
            elif answer.lower() == 'b':
                print('After pumping yourself up, you finally decide to pick a path.')

replay = True

while replay:
    game()
    answer = input('Play again? (Y/N) ')

    if answer.lower() == 'n':
        replay = False
        print('Thank you for playing!')