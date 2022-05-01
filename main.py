def replay(): 
    re = input('Replay? (yes/no) ')
    if re.lower().strip() == 'yes':
        game()
# Create your own adventure with python here
def game():
    print("")
    print('Welcome! You are a monster hunting high school student, and you just got yourself into detention with your monster hunting antics.')
    print("")
    question = input('What day will you go to detention? (monday/friday) ')

    if question.lower().strip() == "monday":
        print("")
        print("(Monday): You walk into the classroom and feel a buzzing in your pocket. It's not your phone though, it's your monster detector! You check it, and it tells you that one of the other students is a Vampire. There are three likely suspects: ")
        print("")
        print("1. Abby, who's drinking a suspicious red liquid")
        print("")
        print("2. Bobby, who's teeth are looking very sharp")
        print("")
        print("3. Connor, who's wearing a large hoodie")
        print("")
        question = input("You take out your garlic to test out your fellow students. But if the vampire notices what you're doing, you're toast. Who do you approach first? (abby/bobby/connor) ")
        if question.lower().strip() == "abby":
            print("")
            print('You walk up to Abby and ...')
            print("")
            print("Turns out Abby was drinking tomato juice, and now you can see Bobby staring at you in the window's reflection. The jig is almost up!")
            print("")
            question = input("You've got one more shot, who do you approach? (bobby/connor) ")
            if question.lower().strip() == "bobby":
                print("")
                print("You walk up to Bobby and ...")
                print("")
                print("Bobby just had in his prop fangs! You realize now that you didn't see Connor's reflection in the mirror, but it's too late. Looks like you better get use to the taste of blood.")
                replay()
            elif question.lower().strip() == "connor":
                print("")
                print("You walk up to Connor and ...")
                print("")
                print("Connor starts shaking uncontrollably as soon as the garlic gets near. The next thing you know, a bat is flying out the window, and nothing but a hoodie is left behind. You survived detention!")
                replay()
        elif question.lower().strip() == "bobby":
            print("")
            print("You walk up to Bobby and ...")
            print("")
            print("Bobby just had in his prop fangs, and now you now you can see Abby staring at you in the window's reflection. The jig is almost up!")
            print("")
            question = input("You've got one more shot, who do you approach? (abby/connor) ")
            if question.lower().strip() == "abby":
                print("")
                print('You walk up to Abby and ...')
                print("")
                print("Turns out Abby was drinking tomato juice... You realize now that you didn't see Connor's reflection in the mirror, but it's too late. Looks like you're going to need a new dental plan.")
                replay()
            elif question.lower().strip() == "connor":
                print("")
                print("You walk up to Connor and ...")
                print("")
                print("Connor starts shaking uncontrollably as soon as the garlic gets near. The next thing you know, a bat is flying out the window, and nothing but a hoodie is left behind. You survived detention!")
                replay()
        elif question.lower().strip() == "connor":
            print("")
            print("You walk up to Connor and ...")
            print("")
            print("Connor starts shaking uncontrollably as soon as the garlic gets near. The next thing you know, a bat is flying out the window, and nothing but a hoodie is left behind. You survived detention!")
            replay()
        else: 
            print("")
            print("Invalid target! You run away, and leave the vampire hunting to someone else.")
            replay()

    elif question.lower().strip() == "friday":
        print("")
        print("(Friday): You walk into the classroom and feel a buzzing in your pocket. It's not your phone though, it's your monster detector! You check it, and it tells you that one of the other students is a Shapeshifter. There are three likely suspects: ")
        print("")
        print("1. Andrea, who's blue eyes are green today")
        print("")
        print("2. Barry, who's olive skin tone is pale today")
        print("")
        print("3. Carla, who's blond hair is red today")
        print("")
        question = input("You take out your silver necklace to test out your fellow students. But if the shapeshifter notices what you're doing, you're deadmeat. Who do you approach first? (andrea/barry/carla) ")
        if question.lower().strip() == "andrea":
            print("")
            print('You walk up to Andrea and ...')
            print("")
            print("Turns out Andrea has in contacts, and now the pale Barry and the brunette Carla are looking this way. The jig is almost up!")
            print("")
            question = input("You've got one more shot, who do you approach? (barry/carla) ")
            if question.lower().strip() == "barry":
                print("")
                print("You walk up to Barry and ...")
                print("")
                print("Barry had a fever and wasn't able to play sports this week. You realize now that Carla's hair changed color, but it's too late. Looks like you'll be missing lunch.")
                replay()
            elif question.lower().strip() == "carla":
                print("")
                print("You walk up to Carla and ...")
                print("")
                print("Carla starts shaking uncontrollably as soon as the silver gets near. The next thing you know, a red bird is flying out the window. You survived detention!")
                replay()
        elif question.lower().strip() == "barry":
            print("")
            print("You walk up to Barry and ...")
            print("")
            print("Barry had a fever and wasn't able to play sports this week, and now the blue eyed Andrea and the brunette Carla are looking this way. The jig is almost up!")
            print("")
            question = input("You've got one more shot, who do you approach? (andrea/carla) ")
            if question.lower().strip() == "andrea":
                print("")
                print('You walk up to Andrea and ...')
                print("")
                print("Turns out Andrea has in contacts. You realize now that Carla's hair changed color, but it's too late. Looks like you're on the menu today. ")
                replay()
            elif question.lower().strip() == "carla":
                print("")
                print("You walk up to Carla and ...")
                print("")
                print("Carla starts shaking uncontrollably as soon as the silver gets near. The next thing you know, a red bird is flying out the window. You survived detention!")
                replay()
        elif question.lower().strip() == "carla":
            print("")
            print("You walk up to Carla and ...")
            print("")
            print("Carla starts shaking uncontrollably as soon as the silver gets near. The next thing you know, a red bird is flying out the window. You survived detention!")
            replay()
        else: 
            print("")
            print("Invalid target! You run away, and leave the shapeshifter hunting to someone else.")
            replay()

    else: 
        print("")
        print("Invalid answer! Looks like you just got expelled! (Game Over)")
        replay()

game()


