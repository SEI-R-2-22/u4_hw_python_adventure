# What do you want to do after highschool?
def start():
    name = input('Enter your name')
    print('Hello ' + name)

    answer_1 = input('What would you like to do after highschool? Type 1 for college, 2 for trade school or 3 for military.')
    if answer_1 == '1':
        print("You've chosen to go to college.")
        answer_2 = input("Do you want to go to a public or private school? Type 1 for public or 2 for private.")
        if answer_2 == '1':
            print("You've chosen to go to a public school.")
            answer_3 = input("Now, do you want to go to a school in state or out-of-state? Type 1 for in-state or 2 for out-of-state.")
            if answer_3 == '1':
                print("You've chosen to go to an in-state school")
                answer_4 = input("What school do you want to go to?")
                print("Congratulations! You have been accepted to " + answer_4)
                return start()
            if answer_3 == '2':
                print("You've chosen to go to an out-of-state school.")
                answer_4 = input("What school do you want to go to?")
                print("Congratulations! You have been accepted to " + answer_4)
                return start()
        if answer_2 == '2':
            print("You've chosen to go to a private school.")
            answer_3 = input("Now, do you want to go to a school in state or out-of-state? Type 1 for in-state or 2 for out-of-state.")
            if answer_3 == '1':
                print("You've chosen to go to an in-state school")
                answer_4 = input("What school do you want to go to?")
                print("Congratulations! You have been accepted to " + answer_4)
                return start()
            if answer_3 == '2':
                print("You've chosen to go to an out-of-state school.")
                answer_4 = input("What school do you want to go to?")
                print("Congratulations! You have been accepted to " + answer_4)
                return start()
    if answer_1 == '2':
        print("You've chosen to go to trade school.")
        answer_5 = input("What trade school do you want to go to? Type 1 for carpentry, 2 for cosmetology or 3 for culinary arts.")
        if answer_5 == '1':
            print("You've chosen to go to carpentry school.")
            answer_6 = input("What length program are you looking for? Type 1 for 9 months, 2 for 12 months or 3 for 24 months.")
            if answer_6 == '1':
                print("Congratulations! You've been accepted into the 9 month long program.")
                return start()
            if answer_6 == '2':
                print("Congratulations! You've been accepted into the 12 month long program.")
                return start()
            if answer_6 == '3':
                print("Congratulations! You've been accepted into the 24 month long program.")
                return start()
        if answer_5 == '2':
            print("You've chosen to go to cosmetology school.")
            answer_7 = input("What kind of specialty do you want to go into? Type 1 for makeup, 2 for hairstyling or 3 for nails.")
            if answer_7 == '1':
                print("Congratulations! You've been accepted into the makeup specialty classes!")
                return start()
            if answer_7 == '2':
                print("Congratulations! You've been accepted into the hairstyling specialty classes!")
                return start()
            if answer_7 == '3':
                print("Congratulations! You've been accepted into the nails specialty classes!")
                return start()
        if answer_5 == '3':
            print("You've chosen to go to culinary school.")
            answer_8 = input("What kind of cuisine are you looking into specializing in? Type 1 for Italian, 2 for American or 3 for Japanese.")
            if answer_8 == '1':
                print("You've chosen to specialize in Italian cusine.")
                answer_9 = input("What is the first dish you want to perfect? Type 1 for ceviche, 2 for risotta or 3 for gelato.")
                if answer_9 == '1':
                    print("You will be focusing on how to make the best ceviche.")
                    return start()
                if answer_9 == '2':
                    print("You will be focusing on how to make the best risotto.")
                    return start()
                if answer_9 == '3':
                    print("You will be focusing on how to make the best gelato.")
                    return start()
            if answer_8 == '2':
                print("You've chosen to specialize in American cuisine.")
                answer_10 = input("What is the first dish you want to perfect? Type 1 for steak or 2 for buffalo wings.")
                if answer_10 == '1':
                    print("You will be focusing on how to make the best steak.")
                    return start()
                if answer_10 == '2':
                    print("You will be focusing on how ot make the best buffalo wings.")
                    return start()
            if answer_8 == '3':
                print("You've chosen to specialize in Japanese cuisine.")
                answer_11 = input("What is the first dish you want to perfect? Type 1 for ramen or 2 for sushi.")
                if answer_11 == '1':
                    print("You have chosen to perfect ramen.")
                    return start()
                if answer_11 == '2':
                    print("You have chosen to perfect sushi.")
                    answer_12 = input("What type of sushi is your favorite?")
                    answer_13 = input("Would you like to learn how to make " + answer_12 + "? Type 1 for yes or 2 for no.")
                    if answer_13 == '1':
                        print("We will be learning how to make " + answer_12 + " sushi!")
                        return start()
                    if answer_13 == '2':
                        print("In that case, let's begin with leaning how to cut sashimi.")
                        return start()
    if answer_1 == '3':
        print("You've chosen to join the military.")
        answer_14 = input("What branch do you want to join? Press 1 for Marine Corps, 2 for Army, 3 for Navy or 4 for Air Force.")
        if answer_14 == '1':
            print("Thank you for joining the Marine Corps! Thank you for your service.")
            return start()
        if answer_14 == '1':
            print("Thank you for joining the Army! Thank you for your service.")
            return start()
        if answer_14 == '1':
            print("Thank you for joining the Navy! Thank you for your service.")
            return start()
        if answer_14 == '1':
            print("Thank you for joining the Air Force! Thank you for your service.")
            return start()

start()


