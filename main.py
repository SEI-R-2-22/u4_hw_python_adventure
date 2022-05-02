# Create your own adventure with python here

def playAgain():
    answer = input("You wanna play again? Type 'play'")
    if answer == 'play':
        startGame()

def invalid():
    print("Error try again")

def startGame():
    print("Hello, today I'm going to help you pick an exciting vacation destination")
    weather = input("Lets start with temperature. Do you want to go somewhere hot? | 'yes' or 'no'")
    if weather == 'yes':
        continent = input("Which of these continents would you like to go to?| Africa | Australia | South America | ")
        if continent == 'Africa':
            trip = input("What sounds like fun? 1. Relaxing by the beach or 2. Trying out some new foods | Enter number of your choice")
            if trip == '1':
                print("You're headed to Mombasa, Kenya! Here you'll find clear beaches and never ending sunshine")
                playAgain()
            elif trip == '2':
                print("Welcome to Egypt! Home to some of the best street food in all of Africa")
                playAgain()
        elif continent == 'Australia':
            trip = input("What sounds like more fun? 1. Visiting the zoo or 2. Surfing | Enter number of your choice ")
            if trip == '1':
                print("Wlecome to Melbourne, Australia! While here check out the Melbourne Zoo")
                playAgain()
            elif trip == '2':
                print("Pack your bags because you're going surfing along the Gold Coast of Australia!")
                playAgain()
        elif continent == 'South America':
            trip = input("What sounds like more fun? 1. Attending a festival 2. Visiting a museum | Enter number of your choice")
            if trip == '1':
                print("Welcome to Brazil! Home to one of the biggest festivals in the world in the Rio Carnival")
                playAgain()
        else:
            invalid()
            playAgain()

    elif weather == 'no':
        continent = input("Which of these continents would you like to go to?| Asia | Europe | North America |")
        if continent == 'Asia':
            trip = input("What sounds like more fun? 1. Swimming with whale sharks 2. Hiking up a mountain | Enter number of your choice ")
            if trip == '1':
                print("Welcome to Cebu, Philippines")
                playAgain()
            elif trip == '2':
                print("Welcome to Sichuan Province, China ")
                playAgain()
            else:
                invalid()
                playAgain()
        elif continent == 'Europe':
            trip = input("What sounds like more fun? 1. Shopping 2. Skiing | Enter number of your choice")
            if trip == '1':
                print("Welcome to Paris")
                playAgain()
            elif trip == '2':
                print("Welcome to the Dolomites of Italy!")
                playAgain()
            else:
                invalid()
                playAgain()
        elif continent == 'North America':
            trip = input("What sounds like more fun? 1. Partying 2. Site-Seeing | Enter number of your choice")
            if trip == '1':
                print("Welcome to Miami, Florida")
                playAgain()
            elif trip == '2':
                print("Wlecome to New York City!")
                playAgain()
        else:
            invalid()
            playAgain()
    else:
        invalid()
        playAgain()

startGame()