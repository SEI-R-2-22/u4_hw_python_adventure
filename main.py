def start_game():
    response = input(
        "Let's head to the grocery store. (y/n) ")

    if response.lower().strip() == 'y':

        response = input(
            'Where would you like to start? (dairy/meat/produce/frozen) ').lower().strip()
        if response == 'dairy':
            response = input('Sweet, do you like yogurt? (y/n) ')
            if response == 'y':
                print('Nice, me too. Im a fan of greek yogurt ')
            else:
                print("Nah? Okay, let's get some milk then ")
                return start_game()

        elif response == 'meat':
            response = input(
                "Nice, are you more of a steak fan or pork tenderloin fan? (steak/pork) ").lower().strip()
            if response == 'steak':
                print("Sick! We should grab 2! ")
            else:
                print("Nice, let's grab a marinated one for dinner. ")
                return start_game()

        elif response == 'produce':
            response = input(
                "Let's get the makings for a salad. Do you want romaine or spinach? (romaine/spinach) ").lower().strip()
            if response == 'romaine':
                print("That's perfect, that's my favorite ")
            else:
                print('Alright, I guess ')
                return start_game()

        elif response == 'frozen':
            response = input(
                "Do you want to grab ice cream or popsicles? (ice_cream/popsicle) ").lower().strip()
            if response == 'ice_cream':
                print("Dopeeee I love my some ice cream! ")
            else:
                print("What are you, five? ")
                return start_game()

    else:
        print("You stay home and refuse to accept that you're now an adult")


start_game()