starting = input(
    "Hello, you have arraived to the food court area, you have 2 optitons type a to go to Burger restaurant type b to go to Seafood restaurant? "
)


def main():

    choice = str(starting)
    if choice == 'a':
        input("You chose the Burgers restaurant, now you can choose to check the menu type a or leave the restaurant type b? ")
        choice2 = str(choice)
        if choice2 == 'a':
            int(input("Here is the menu, it has 2 main meals /n 1- Classic Burger with fires and salad /n 2- Double Cheese Burger with mashed potatoes and ice cream /n please chose 1 or 2"))
            print('Enjoy your meal')
        else:
            print('Have a good day!!')
    else:
        input("You chose the Seafood restaurant, now you can choose to check the menu type a or leave the restaurant type b? ")
        choice3 = str(starting)
        if choice3 == 'b':
            int(input("Here is the menu, it has 2 options, /n 1- Grilled Lobster with vegetables /n 2- King Crab with white rice /n please pick 1 or 2 "))
            print('Enjoy your meal')
    answer = int(input(
        "We got to the end of the journey here, would you like to revisit those restaurants (yes/no) ? "))
    if answer.lower().strip() == "yes":
        main()
    else:
        print('Have Great day !!!')


main()
