# Create your own adventure with python here
def restart():
    answer = input("What if I told you, this... all this.. is just a dream. Would you believe me? (yes/no)")

    if answer.lower().strip() == 'yes':
        print("... It's a beautiful day and you're walking through the park without a care in the world. All of a sudden when you get this strange feeling that someone is following you...")
        answer = input("Do you Turn around or run? (turn/run)" ).lower().strip()
        if answer == 'turn':
            answer = input("NO! SAY it aint so!! It's your biggest fear, half snake half spider half wasp. Do you RUN or FIght? (Run/Fight)").lower().strip()
            if answer == "run":
                answer = input("You're running but it seems like your in quick sand. The Beast is getting closer. Do you Fight, hide in the nearby bush, or jump into the river?(fight/jump)" ).lower().strip()
                if answer == 'fight':  
                    print("You've slayed the beast. To your surprise, you're an expert fighter... Almost too good... Is this a dream?")
                    return restart()
                elif answer == 'jump':
                    answer = input('You jump in the stream but you sink like a ton of bricks. You cant breath and you start to see a bright light. Do you reach for the light or fall into the darkness?(light/dark)').lower().strip()
                    if answer == 'light':
                        print("Whoa, I'm in my bed. I guess this was all a dream. But why do i have hoofs as hands??!?")
                        return restart()
                else:
                    print("It's very dark and very cozy and almost feels like you're in a dream...")
                    return restart()
            elif answer == 'fight':
                print("You've slayed the beast. To your surprise, you're an expert fighter... Almost too good... Is this a dream?")
                return restart()
        elif answer == "run":
            print("You try to run but your feet are stuck to the floor like a mouse in a glue trap.")
            answer = input("Stuck like a mouse you have two options. Try to fight this monster or play dead and hope it doesn't bother you. (fight/play dead)").lower().strip()
            if answer == 'fight':
                print("The beast is coming closer and all of a sudden if feels like gravity has made your arms as heavy as an anvil. Which is weird because this only happens when im drea...")
                return restart()
            else:
                print("It seams like that worked. The beast walked right past you. What was that beast doing in the park? This has to make the news right? Wait a second...")
                return restart()  
        else:
            print("Oh.. i forgot to tell you. This is an infinte dream. Nothing you can do will break this loop. Welcome to limbo")
            return restart()          
    else:
        print("Sorry you are drifting into REM! Sit back and enjoy the magic.") 
        return restart()

restart()          