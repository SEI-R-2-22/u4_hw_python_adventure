# Create your own adventure with python here
import time

def finalizeFunc(weapon, location, alignment):
    print("Interesting choice.. you chose " + alignment + ".\nLastly, what food do you enjoy most?\n1.) Sandwiches\n2.) Pizza\n3.) Pretzals")
    food = input()
    if int(food) == 1:
        food = "sandwiches"
        print("Perfect! Here's your story!\n You are a warrior of " + alignment + " who has come to the " + location + " to take back all the " + food + ". Using your trusty " + weapon + ", you dispatch all foes. You are named King/Queen of " + food + " " + location + "! Congrats!")
        time.sleep(5.0)
        print("Play again?\n1.)Yes\n2.)No")
        restart = input()
        if int(restart) == 1:
            main()

        elif int(restart) == 2:
            exit()

    elif int(food) == 2:
        food = "pizza"
        print("Perfect! Here's your story!\n You are a warrior of " + alignment + " who has come to the " + location + " to take back all the " + food + ". Using your trusty " + weapon + ", you dispatch all foes. You are named King/Queen of " + food + " " + location + "! Congrats!")
        time.sleep(5.0)
        print("Play again?\n1.)Yes\n2.)No")
        restart = input()
        if int(restart) == 1:
            main()

        elif int(restart) == 2:
            exit()

    elif int(food) == 3:
        food = "pretzals"
        print("Perfect! Here's your story!\n You are a warrior of " + alignment + " who has come to the " + location + " to take back all the " + food + ". Using your trusty " + weapon + ", you dispatch all foes. You are named King/Queen of " + food + " " + location + "! Congrats!")
        time.sleep(5.0)
        print("Play again?\n1.)Yes\n2.)No")
        restart = input()
        if int(restart) == 1:
            main()

        elif int(restart) == 2:
            exit()

    else:
        print("Unknown command.")
        time.sleep(5.0)
        main()
    


def alignmentFunc(weapon, location):
    print("Perfect! You chose " + location + ".\nAre you good or evil?\n1.) Good\n2.) Evil")
    align_choice = input()
    if int(align_choice) == 1:
        alignment = "good"
        finalizeFunc(weapon, location, alignment)
    elif int(align_choice) == 2:
        alignment = "evil"
        finalizeFunc(weapon, location, alignment)

def locationFunc(weapon):
    print("Great! You chose " + weapon + ".\nNow, where would you like to fight?\n1.) Castle\n2.) Dungeon")
    location = input()
    if int(location) == 1:
        location = "castle"
        alignmentFunc(weapon, location)

    elif int(location) == 2:
        location = "dungeon"
        alignmentFunc(weapon, location)

    else:
        print("Selection error. Please try again.")
        main()
    







def adventure():
    print("What is your weapon of choice?\n1.) Sword\n2.) Mace\n3.) Spear")
    weap_choice = input()
    if int(weap_choice) == 1:
        weapon = "sword"
        locationFunc(weapon)
        

    elif int(weap_choice) == 2:
        weapon = "mace"
        location = locationFunc(weapon)
        

    elif int(weap_choice) == 3:
        weapon = "spear"
        location = locationFunc(weapon)
        

    else: 
        print("Weapon choice not viable. Please try again.")
        time.sleep(5.0)
        main()
    
    
    
    


def main(): 
    print('Welcome to Fantasy Py!\nPlease make each choice using the corresponding number associated with your choice. (1,2,3)\nPress 1 to begin!')
    choice = input()
    if int(choice) is 1:
        adventure()

    else: 
        main()


main()
