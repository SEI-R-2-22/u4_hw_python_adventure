# Create your own adventure with python here

def game_play():
    print('Hello there, I am the Mirror of Erised. Only "Harry Potter" can enter. Remember, you have to enter your words EXACTLY as you are prompted, case sensitive and all...')
    name = input('Identify yourself: ')
    print('Hello there, I am the Mirror of Erised. Only "Harry Potter" can enter. ' + name)

    if name == 'Harry Potter':
        search_item = input(
            'Are you searching for your "Friends" or the "Horcruxes" today?: ')
        print('Nice to meet you, Harry Potter. I can only help you find your friends or the remaining horcruxes' + search_item)

        if search_item == 'Friends':
            friend_name = input(
                'Would you be searching for "Ron", "Hermoine" or "Neville" today, Master Potter?: ')
            print(friend_name)
            if friend_name == 'Ron':
                print(
                    'Unfortunately, Ron is useless and cannot help you. Please return to start')
                game_play()

            elif friend_name == 'Hermoine':
                hermoine_location = input(
                    'Where would you like to look for Hermoine?: ')
                print(
                    'We can look in "Aritmancy Class", "Library", or in the "Gryffindor Common Room" ' + hermoine_location)
                if hermoine_location == 'Aritmancy Class':
                    print(
                        'Unfortunately Master Potter, Hermoine is not here. Please return to beginning')
                    game_play()
                elif hermoine_location == 'Library':
                    print('Hermoine to the rescue! Follow Hermoine to find the Horcrux')
                    hermoine = (
                        'You got it! Return to start to play again?: ' + 'Type "y" to restart, or exit game: ')
                    if hermoine == 'y':
                        game_play()
                elif hermoine_location == 'Gryffindor Common Room':
                    print(
                        'Hermoine already left, unfortunately. Please return to beginning')
                    game_play()
                else:
                    print(
                        'Unfortunately, I am unable to search this location. Please return to start')
                    game_play()

            elif friend_name == 'Neville':
                neville_location = input('Where would you like to look?: ')
                print(
                    'We could search for Neville in "Herbology Class", or in the "Room of requirement". ' + neville_location)
                if neville_location == 'Herbology Class':
                    print(
                        'Unfortunately, the class is empty and Neville is not here. Please return to start')
                    game_play()
                elif neville_location == 'Room of Requirement':
                    print("Join Neville in training for Dumbledore's army")
                    neville = (
                        'You got it! Return to start to play again?: ' + 'Type "y" to restart, or exit game: ')
                    if neville == 'y':
                        game_play()

        elif search_item == 'Horcruxes':
            horcrux_count = input(
                'How many Horcruxes would you be seeking today, Master Potter?: ')
            print('There are 3 left. You either have to find all remaining horcruxes, or no horcruxes at all. ' + horcrux_count)
            horcrux_int = int(horcrux_count)

            if horcrux_int == 3:
                horcrux_result = input(
                    'Are you searching for "Nagini", "Tom Riddle`s diary", or the "Secret Horcrux", master Potter?: ')
                print(horcrux_result)
                if horcrux_result == 'Nagini':
                    nagini_location = input(
                        'Would you like to search for Nagini in "Little Rangleton Cemetary" or in "Hogwarts", Master Potter?: ')
                    print(nagini_location)
                    if nagini_location == 'Little Rangleton Cemetary':
                        print('Nagini slithered away. Please return to start')
                        game_play()
                    elif nagini_location == 'Hogwarts':
                        print('Nagini is at Hogwarts! Draw your swords!!!')
                        nagini = (
                            'You got it! Return to start to play again?: ' + 'Type "y" to restart, or exit game: ')
                        if nagini == 'y':
                            game_play()
                    else:
                        print(
                            'Nagini cannot be reached in this location. Please return to start')
                        game_play()

                if horcrux_result == "Tom Riddle's Diary":
                    riddle_location = input(
                        'You can choose to search for Tom Riddle`s diary either in the "Chamber of Secrets", or in the "Library". Where would you like to look, Master Potter?: ')
                    print(riddle_location)
                    if riddle_location == 'Library':
                        print(
                            "Tom Riddle's diary has been moved. Please return to start")
                        game_play()
                    elif riddle_location == 'Chamber of Secrets':
                        print(
                            'The diary was already destroyed in the Chamber of Secret. Return to Start')
                        game_play()
                    else:
                        print(
                            'Nagini cannot be reached in this location. Please return to start')
                        game_play()
            else:
                print(
                    'You have chosen the wrong number of horcrux. Please return to start and try again.')
                game_play()

        else:
            print('I am sorry I cannot help you. Please return to start')

    else:
        print('You are not Harry Potter. Please exit and begin game again')


print(game_play())
