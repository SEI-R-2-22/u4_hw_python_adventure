# Create your own adventure with python here
def thirdChoiceD(choice):
    if choice == 1:
        print("After a beat the voice replies calmly 'Not anymore'.  The emerald glows solid and you watch as it dissolves into your hand.  Green striations run up your arm like veins, spreading quickly tot he rest of your body.  You feel different.  Powerful.  But most strangely, unconcerned with what just occurred.  You drop the worms, you're not hungry anymore.  You don't know where you're headed, but someone does.")
        print('The End. Press 1 to play again')
        next_choice = int(input())
        if next_choice == 1:
            beginGame()
        else:
            print('You can exit with ctrl/command+c')
    elif choice == 2:
        print("Halfway through your proud introduction the voice screams 'BORING!' The emerald glows and flies high up into the air and out of site. You are disappointed you didn't get to talk about your run in with the bugbear.")
        print('The End. Press 1 to play again')
        next_choice = int(input())
        if next_choice == 1:
            beginGame()
        else:
            print('You can exit with ctrl/command+c')


def thirdChoiceC(choice):
    if choice == 1:
        print("After 10 or so minutes you feel a strong pull on the line.  Suddenly alert, you begin to reel in at specific intervals, prompted by tension changes in the line.  After some expert fishmanship(?) you pull out a beautiful looking fish.  You'll eat well tonight.")
        print('The End. Press 1 to play again')
        next_choice = int(input())
        if next_choice == 1:
            beginGame()
        else:
            print('You can exit with ctrl/command+c')
    elif choice == 2:
        print("You decide to put your rod away and just as you finish doing so a fish jumps out from the water and slaps you in the face.  You become enraged and have a heart attack, falling into the river. You died")
        print('The End. Press 1 to play again')
        next_choice = int(input())
        if next_choice == 1:
            beginGame()
        else:
            print('You can exit with ctrl/command+c')


def thirdChoiceB(choice):
    if choice == 1:
        print("'That was awesome!'  you exclaim to no one.  Turning around and looking at the river you let out a celebratory woop just before being hit in the back of the head with a rock.  You died.")
        print('The End. Press 1 to play again')
        next_choice = int(input())
        if next_choice == 1:
            beginGame()
        else:
            print('You can exit with ctrl/command+c')
    elif choice == 2:
        print("As you look around you notice your wild entrance has startled someone.  There is a man in the tree above you loading his sling.  You call out and say 'I mean no harm!'  The two of you get tot talking, hunt and cook a nice meal then go your separate ways.")
        print('The End. Press 1 to play again')
        next_choice = int(input())
        if next_choice == 1:
            beginGame()
        else:
            print('You can exit with ctrl/command+c')


def thirdChoiceA(choice):
    if choice == 1:
        print("You decide to rest for a moment and promptly fall asleep until the next morning.  You find all of your effects are missing and you've been left a note 'How come I always catch you sleeping on the job? -J' Exasperated you look to the sun for direction and begin to make your way towards the coastal town you know is nearby.  Well, you HOPE it's nearby.")
        print('The End. Press 1 to play again')
        next_choice = int(input())
        if next_choice == 1:
            beginGame()
        else:
            print('You can exit with ctrl/command+c')
    elif choice == 2:
        print("Reluctantly you rise and keep heading on your way.  Sooner than you expect you see your destination rise on the horizon, preceded by the huge canvas sails of the ships in the harbor.  You smile knowing an ale is waiting for you at your favorite tavern.  Things could be worse.")
        print('The End. Press 1 to play again')
        next_choice = int(input())
        if next_choice == 1:
            beginGame()
        else:
            print('You can exit with ctrl/command+c')


def secondChoiceB(choice):
    if choice == 1:
        print("You pull out your lucky lure and attach it to your line, double checking your knot.  You think for a moment about why this is your lucky lure and realize as you cast it is your only lure. No bites yet, water looks still.")
        print('Type 1 to wait.  Type 2 to give up')
        next_choice = int(input())
        thirdChoiceC(next_choice)
    elif choice == 2:
        print('You find some soft damp soil on the bank and begin to dig.  You manage to find a handful of good sized worms before your finger strikes something hard and smooth.  You find your hand grasping a cloudy emerald sphere that begins to pulse with light in the center.  Each pulse grows brighter and you hear a cacophony of whispers in your head.  They grow louder and more disharmonious until they converge on a single shout.  "WHO ARE YOU?"')
        print(
            'Type 1 to say "Nobody".  Type 2 to produly state your adventuring credentials.')
        next_choice = int(input())
        thirdChoiceD(next_choice)
    else:
        beginGame()


def secondChoiceA(choice):
    if choice == 1:
        print('Reacting quickly, you begin to swim your way to the opposite shore.  The rivers current is much stronger than you thought and you think you may have over-exerted yourself a bit.  Breathing heavy, you drag yourself up the muddy bank and seat yourself facing the now dilapidated bridge.')
        print('Type 1 to Rest.  Type 2 to Continue')
        next_choice = int(input())
        thirdChoiceA(next_choice)
    elif choice == 2:
        print("Staying calm, you relax and begin to float on your back.  You're careful to keep an eye out for large rocks but the way seems relatively clear.  After a few minutes you see the river bend ahead of you.  Utilizing the speed from the river you bend your knees, plant your feet, and stand up on the river bank.")
        print('Type 1 to admire your prowess.  Type 2 to get your bearings')
        next_choice = int(input())
        thirdChoiceB(next_choice)
    else:
        beginGame()


def firstChoice(choice):
    if choice == 1:
        print('You decide to continue on your way.  When you reach the middle of the bridge there is a sudden, terrible groan from the old wood below.  After a few more creaks and moans, the bridge has given up on you.  You have plunged into the river.')
        print('Type 1 to swim to shore.  Type 2 to go with the flow')
        next_choice = int(input())
        secondChoiceA(next_choice)
    elif choice == 2:
        print('Assembling your rod is a less a habit than part of your reflexes.  Time to choose a lure.  Or should you dig for worms?')
        print('Type 1 to use a lure.  Type 2 to dig for worms')
        nextChoice = int(input())
        secondChoiceB(nextChoice)
    else:
        beginGame()


def beginGame():
    print('While walking along the road one day, you suddenly come upon a bridge crossing over a flowing river.  You could continue on your way, but you also think this could be a fortuitous fishing spot.')
    print('Type 1 to cross the bridge.  Type 2 to Go fishing')
    choice = int(input())
    firstChoice(choice)


beginGame()
