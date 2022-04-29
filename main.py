# Create your own adventure with python here


is_playing = 'Y'


def play(username):
    confirm = input('Are you ready to play, ' + username + '? Y/N\n')

    if confirm == "Y":
        movie = input(
            'Are you a fan of Harry Porter or Lord of the Rings?(H/L)\n')
        if movie == 'H':
            movie_char = input(
                'Which character you would like to be?\nHarry Potter(HP), Ron Weasley(RW) Or Hermione Granger(HG)\n')
            if movie_char == 'HP':
                wand = input(
                    'Your enemy is voldemort, which wand would you choose, Elder Wand or Original Wand?(E/O)\n')
                if wand == 'E':
                    print("With Elder Wand, you defeated Voldemort!\n")
                else:
                    print('Your wand was broke by Voldemont!\n')
            elif movie_char == 'RW':
                battle = int(input(
                    'Which battle would you want to play?\nBattle of the Department of Mysteries(1), Battle of the Astronomy Tower(2), or Battle of the Seven Potters(2)\n'))
                if battle == 1:
                    print('Open war is declared on the wizarding community. Ministry of Magic accepts that Voldemort has returned The prophecy is destroyed. Death of Sirius Black. All Death Eaters except Voldemort and Bellatrix are arrested.\n')
                elif battle == 2:
                    print('Albus Dumbledore killed. Minor to major injuries of several of Hogwarts\' defenders. Draco Malfoy unknowingly becomes master of the Elder Wand. Snape becomes headmaster of Hogwarts.\n')
                elif battle == 3:
                    print('Death Eaters\' short term victory because of the death of Alastor Moody. Harry Potter is successfully transported to The Burrow. Long-term strategic effects favourable to the Order of the Phoenix.\n')
                else:
                    print("You don't want to go to battle.\n")
            elif movie_char == 'HG':
                clever = input("Do you think you're a little clever? Y/N\n")
                if clever == 'Y':
                    print('You\'re truely talented.\n')
                else:
                    print('You have so much doubts in yourself.\n')
            else:
                print('You must love playing all of them!\n')
        else:
            is_precious = input('Have you heard "My precious!"?Y/N\n')
            if is_precious == 'Y':
                movie_char = int(input(
                    'Which character you would like to be? Frodo Baggins(1), Samwise Gamgee(2), Bilbo Baggins(3), Aragorn(4), Gandalf(5), Legolas(6) or Gimli(7)\n'))
                if movie_char == 1:
                    print(
                        'I wish the Ring had never come to me. I wish none of this had happened.\n')
                elif movie_char == 2:
                    print('I think, Mr. Frodo, I do understand. I know now. Folk in those stories had lots of chances of turning back only they didn\'t. Because they were holding on to something.\n')
                elif movie_char == 3:
                    print('Never laugh at live dragons!\n')
                elif movie_char == 4:
                    print('There is always hope.\n')
                elif movie_char == 5:
                    print(
                        'All we have to decide is what to do with the time that is given us.\n')
                elif movie_char == 6:
                    print(
                        'The way is shut. It was made by those who are dead, and the dead keep it. The way is shut.\n')
                elif movie_char == 7:
                    print(
                        'Let Them Come! There Is One Dwarf Yet In Moria Who Still Draws Breath!\n')
                else:
                    print('My precious!\n')
            else:
                print('You are not a fan of Lord of the Rings!\n')


username = input("Welcome to the wizard world!\nWhat's your name?\n")

while is_playing == 'Y':
    print(is_playing)
    play(username)
    is_playing = input('Would you like to play again?Y/N\n')
