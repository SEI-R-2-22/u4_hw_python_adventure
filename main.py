def game():    
    question = input('Hi. Welcome to Space Colony 7. Would you like to go in the (s)huttle down to the planet, go to (m)ain deck, visit the (c)ommissary or go back to your (r)oom? ')    
    if str(question) == "s":
        question = input('Shuttle! Great choice. You are on the planet. Do you go into the (v)illage or go for a (s)wim? ' )
        if str(question) == "v":
            question = input('You go to the village. Do you go to the market or go to the opera? ')
            if str(question) == "m":
                question = input('You went to the market and bought a space pony. Would you like to restart the game? (yes or no) ')
                if str(question) == "yes": 
                    game()
                else:
                    print('OK, see you later. Thanks for playing')                
            else:
                question = input('You went to the opera and had a grand time You now appreciate opera. Would you like to restart the game?? (yes or no) ')
                if str(question) == "yes": 
                    game()
                else:
                    print('OK, see you later. Thanks for playing') 
        else:
            question = input('You go for a refreshing swim and meet an alien in a bikini. Do you: ask them on a (d)ate or go to the (s)ouvenir shop?. ')
            if str(question) == "d":
                question = input('You go to a nice wine bar and have a nice date. Then you marry them and have half alien children together. Would you like to restart? (yes or no) ')
                if str(question) == "yes": 
                    game()
                else:
                    print('OK, see you later. Thanks for playing')                
            else:
                question = input('You find a nice t-shirt and buy it to bring home to your mom. Would you like to restart? (yes or no) ')
                if str(question) == "yes": 
                    game()
                else:
                    print('OK, see you later. Thanks for playing')         
    elif str(question) == "m": 
        question = input('Main deck! Sounds good You have answered one question. Do you ask to (f)ly the ship or do you ask to (c)ontrol the transporter ')
        if str(question) == "f":
            question = input('You nearly crash the ship into an alien ship. They are mad and start posturing for battle. Do you (e)vade or (f)ight? ')
            if str(question) == "e":
                question = input('You barely get away but live to tell the tale. You are lauded as a hero. Would you like to restart? (yes or no) ')
                if str(question) == "yes": 
                    game()
                else:
                    print('OK, see you later. Thanks for playing')                
            else:
                question = input('Your ship fires its weapons. Their ships fires theirs. Your ship blows up. Womp womp. The End. Would you like to restart? (yes or no) ')
                if str(question) == "yes": 
                    game()
                else:
                    print('OK, see you later. Thanks for playing')    
        else:
            question = input('You accidentally beam a tribble onto the main deck Do you (b)eam it somewhere else or (k)eep it as a pet? ')
            if str(question) == "b":
                question = input('You narrowly avoided an infestation! No one notices your herocism but believe be, you are the winner. Would you like to restart? (yes or no) ')
                if str(question) == "yes": 
                    game()
                else:
                    print('OK, see you later. Thanks for playing')                
            else:
                question = input('Uh oh! Your tribble multiplies at an alarming rate and infests the ship. Everyone gets mad at you and you become the laughing stock of the universe. The end.  Would you like to restart? (yes or no) ')
                if str(question) == "yes": 
                    game()
                else:
                    print('OK, see you later. Thanks for playing') 
    
    elif str(question) == "c": 
        question = input('The commissary is filled with strange new food. Do you try the stuff that looks like (j)ello or the stuff that looks like (e)yeballs?  ' )
        if str(question) == "j":
            question = input('The jello tastes like crap! Do you get a (s)andwich or get a (b)eer? ')
            if str(question) == "s":
                question = input('The sandwich is the best you have ever tasted. It even has those fancy toothpicks in each half. The end. Would you like to restart the game? (yes or no) ')
                if str(question) == "yes": 
                    game()
                else:
                    print('OK, see you later. Thanks for playing')                
            else:
                question = input('The beer washes away the sorrow brought on by the jello. This has been a good first day in space. The end. (yes or no) ')
                if str(question) == "yes": 
                    game()
                else:
                    print('OK, see you later. Thanks for playing') 
        else:
            question = input('Wow! This is really delicious! You are satiated and head to the bar for a drink. Do you get a (m)artini or a (s)pace scotch? ')
            if str(question) == "m":
                question = input('Congrats! You have been hired to star in the next James Bond Movie. Good work, 007. Would you like to restart the game? (yes or no) ')
                if str(question) == "yes": 
                    game()
                else:
                    print('OK, see you later. Thanks for playing')                
            else:
                question = input('Something feels funny. You look down and realize you have grown tentacles! Well, at least you will be better at video games now. The end. Would you like to restart? (yes or no) ')
                if str(question) == "yes": 
                    game()
                else:
                    print('OK, see you later. Thanks for playing')         
    else: 
        question = input('Back in your room you realize there is room service. Do you order (s)pace hamburger or a (l)obster? ')
        if str(question) == "s":
            question = input('The hamburger floats in zero G! You wolf it down and think it is great. Now what? Watch (t)v or go for a walk on the (h)ull? ')
            if str(question) == "t":
                question = input('You watch the Ken Burns documentary about space baseball and realize it is actually a pretty great sport. You look forward to going to a game next time you are in the big city. The end.  Would you like to restart? (yes or no) ')
                if str(question) == "yes": 
                    game()
                else:
                    print('OK, see you later. Thanks for playing')                
            else:
                question = input('You put on your zero gravity boots and start to head out for a space walk when your partner Facetimes you. You talk to them for a while and make a plan for them to meet you at the space station. It is going to be a romantic getaway once they arrive ;) The End. Would you like to restart? (yes or no) ')
                if str(question) == "yes": 
                    game()
                else:
                    print('OK, see you later. Thanks for playing')    
        else:
            question = input('Wow. The lobster is from Maine and is just like on Earth. Suddenly you miss home. Do you hop on (g)oogle Earth and relive the nostalgia of your good times on Earth or do you go to the (c)asino to play space blackjack? ')
            if str(question) == "g":
                question = input('Wow! What a trip down memory lane. You realize you actually love life in space but are looking forward to visiting Earth again sometime soon. The end.  Would you like to restart? (yes or no) ')
                if str(question) == "yes": 
                    game()
                else:
                    print('OK, see you later. Thanks for playing')                
            else:
                question = input('You go to the casino and lose all your money. Boo. The end. Would you like to play again? (yes or no) ')
                if str(question) == "yes": 
                    game()
                else:
                    print('OK, see you later. Thanks for playing') 
game()
    
