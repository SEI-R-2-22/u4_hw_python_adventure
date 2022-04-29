# Create your own adventure with python here
def restart():
    answer = input(
        'Welcome to my coffee shop, Do you want order anything to drink? ☕️ (y/n)')

    if answer.lower().strip() == 'y':

        answer = input(
            'We have: IcedCoffee, Latte, Frappuccino, Mocha. What would you like?').lower().strip()
        if answer == 'icedcoffee':
            answer = input('do you like milk in your icedcoffee? (y/n)')
            if answer == 'y':
                print('Great choice, we will get your order shortly')
            else:
                print('eww, iced coffee with milk, get out of here')
                return restart()

        elif answer == 'latte':
            answer = input(
                'We have matcha latte and regular latte, which one do you prefer?(matcha/regular)').lower().strip()
            if answer == 'matcha':
                print('Thanks for visiting us, your total is $4.00')
            else:
                print('eww, regular latte? you have to order more')
                return restart()

        elif answer == 'frappuccino':
            answer = input(
                'We have Coffee Frappuccino and Caramel Ribbon Crunch Frappuccino, which one do you prefer?(coffee/caramel)').lower().strip()
            if answer == 'coffee':
                print("That's perfect, this one is on us, comeback later!")
            else:
                print('eww, what? you have to order more')
                return restart()

        elif answer == 'mocha':
            answer = input(
                'We have iced mocha and hot Mocha, choose one(iced/hot)').lower().strip()
            if answer == 'iced':
                print('great choice, you have a great one!')
            else:
                print("eww, what? it's 90 outside. you have to start over")
                return restart()

    else:
        print('You turn around and leave the store')


restart()
