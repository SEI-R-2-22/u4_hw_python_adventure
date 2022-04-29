# Create your own adventure with python here
def start_game():
    start = input(
        "Greetings! You crashed on an alien planet! Press a to explore the area or b to call for help")
    choice = str(start)
    if choice == 'a':
        print("***You went to the jungle. A wild alien animal jumped out and wants to eat you! Run!!!***")
    else:
        print("***It's too hot in the desert, I should go back***")
    
    call = input("You're trying to call for help. Press a to call your base or press b to call your mom")
    choice_two = str(call)
    if choice_two == 'a':
        print("***Oh no! Everyone on the base is on vacation! Nobody answers the phone!***")
    else:
        print("***You should't call your Mom. She'll be upset you forgot your lunch!***")
    hungry = input("You're getting hungry. Too bad you forgot your lunch!Press a to double check your fridge or press b to go out and look for food")
    choice_three = str(hungry)
    if choice_three == 'b':
        print("***You're going to hunt ancient human style! Wait, you're vegetarian and you could not hurt a fly!***")
    else:
        print("***You know very well there's nothing in the fridge, but sure, check three more times.***")

    final = input("You're desperate at this point. Press a to build a raft or press b to try to fix the radio")
    choice_four = str(final)
    if choice_four == 'a':
        print("***That's a stupid idea because there's no water around here!***")
    else:
        print("***You should've payed attention on 'How to fix the Radio lessons! It's not working!***")
    one_more = input("You're angry and you kick the radio really hard and...it works again! Press a to call your bestie, press b to call your Mom")
    last = str(one_more)
    if last == 'a':
            print("***Your bestie starts talking and talking and your battery dies before you ask for help***")
    else:
        print("***After yelling at you for a while, Mom calls for help. Rescue team is on it's way!***")
        play = input("Would you like to play again? press y for yes and n for no")
        again = str(play)
        if again == 'y':
            start_game()
        else:
            print("***Ok go have a drink instead***")
start_game()