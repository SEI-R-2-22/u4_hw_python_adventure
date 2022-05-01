# Create your own adventure with python here


def start_game():
    print("""     Welcome to 'Train Murder Mystery Simulator 3000'
  
  I am the conductor.  There has been a murder aboard the train, and you are the only one who can solve it!  The victim is a famous movie stair.  There looks to be signs of a struggle.  
  
  Please make your way around the cars and speak to the passengers.  I'm sure you will be able to gather enough clues to solve the crime.  Come back to me when you think that you have the mystery solved.
  
  Ready to solve the murder?
  """)
    question_one()


def question_one():
    answer_one = input(
        "Please answer all questions with an option in the paranthesis. (yes/no)")
    if answer_one == 'yes':
        question_two()
    elif answer_one == 'no':
        print("Would you like me to explain again, or do you just not feel like playing anymore?")
        answer_two = input('(explain/quit)')
        if answer_two == 'explain':
            start_game()
        else:
            print('Thanks for playing.  Goodbye.')
    else:
        print('That is not an accepted response.  Please try again')
        question_one()


def question_two():
    print("There are three different cars you can visit, and each car has multiple suspects to question.  Please choose which car to go to first, and good luck!")
    answer_one = input('Where would you like to start?(dining/lounge/cabins)')
    if answer_one == 'dining':
        dining_car()
    elif answer_one == 'lounge':
        lounge_car()
    elif answer_one == 'cabins':
        cabin_car()
    else:
        print('That is not an accepted answer.  Please try again')
        question_two()


def navigate():
    answer_one = input(
        'Which car would you like to go to?(dining/lounge/cabins/conductor)')
    if answer_one == 'dining':
        dining_car()
    elif answer_one == 'lounge':
        lounge_car()
    elif answer_one == 'cabins':
        cabin_car()
    elif answer_one == 'conductor':
        conductor()
    else:
        print('That is not an accepted answer.  Please try again')
        navigate()


def dining_car():
    print("""The dining car has tables of various sizes along each side of the wall.  A quick glance shows that it is mostly empty, except for a newlywed couple and their waitress.  
  
  I guess not many of the guests have an appetite knowing that there was a murder recently.  Funny that these newlyweds don't seemed bothered.  Their waitress, on the other hand, looks a little frazzled.""")
    dining_end()


def dining_end():
    answer = input(
        "What would you like to do?  Talk to (waitress/newlyweds) or (leave)?")
    if answer == 'waitress':
        waitress()
    elif answer == 'newlyweds':
        newlyweds()
    elif answer == 'leave':
        navigate()
    else:
        print('That is not an accepted answer.  Please try again.')
        dining_end()


def waitress():
    print("""You walk up to the waitress who is nervously tapping her foot and fidgeting.
      'Hello', you say.  It seems as if the waitress is so lost in thought that she has not heard you or seen you approach.
      'Hello', you say again.  This time she notices you, and flashes a false smile.

      'Hi, welcome to the dining car.  You can sit at any table you would like.'

      'Thats ok', you say.  'I am just looking for some information on the murder.  You seem a little on edge.  I guess thats to be expected.  Do you have any information about what happened?'

      The waitress looks left and right, and then leans in and says, 'I saw the victim get into an argument with the colonel earlier.  They were shouting about something.  It seemed like the colonel was very mad.  Thats all I know.  I have to get back to my job.'
      """)
    waitress_end()


def waitress_end():
    answer = input(
        'What would you like to do next? Talk to (newlyweds) or (leave)')
    if answer == 'newlyweds':
        newlyweds()
    elif answer == 'leave':
        navigate()
    else:
        print('That is not an accepted answer.  Please try again')
        waitress_end()


def newlyweds():
    print("""You walk up to the newlyweds, who are very much playing the part.  They are sitting next to each other at a small table in the corner.  They seem as if them and their love are the only things that exist in the world.  
  
  You approach them, introduce yourself, and ask to sit down.  They oblige.
  
  You quickly learn that this is indeed their honeymoon, and they will be damned if they let a murder ruin that.
  
  'Can you tell me anything about the murder, perchance?', you ask.
  
  'Not really.  We haven't been very social with the other guests.  You know how it is with newlyweds.  We are just enjoying each others company.
  
  'Thank you for your time.'  You get up and leave.""")
    newlyweds_end()


def newlyweds_end():
    answer = input(
        'What would you like to do next? Talk to (waitress) or (leave)')
    if answer == 'waitress':
        waitress()
    elif answer == 'leave':
        navigate()
    else:
        print('That is not an accepted answer.  Please try again')
        newlyweds_end()


def lounge_car():
    print("""You enter the lounge car and are immediately greeted with the stench of cigar smoke and booze.  There seems to be a heated conversation between the colonel and the politician occuring, while the billionaire is sitting at the bar alone with a drink.""")
    lounge_end()


def lounge_end():
    answer = input(
        'What would you like to do?  Approach the (argument), talk to the (billionaire) or (leave)')
    if answer == 'argument':
        argument()
    elif answer == 'billionaire':
        billionaire()
    elif answer == 'leave':
        navigate()
    else:
        print('That is not an accepted response.  Please try again.')
        lounge_end()


def billionaire():
    print("""You walk up to the bar, void of a bartender, and ask the billionaire if they mind if you join them.
  
  They look at you for a second, emotionless, then grab a glass from behind the bar, fill it, and pass it to you.

  'If you are going to sit and ask your questions, you have to drink', they say.""")
    drink_question()


def drink_question():
    answer = input('What do you do? (drink)? or (decline)')
    if answer == 'drink':
        billionaire_two()
    elif answer == 'decline':
        print("""You politley thank them, but decline the drink.
    'Then we have nothing to talk about', they say as they turn back to their drink.
    You try to start the conversation again, but they just side eye you.  You think its best to leave, and you do.""")
        lounge_end()
    else:
        print('That is not an accepted response.  Please try again.')
        drink_question()


def billionaire_two():
    print("""You tap their glass and take a swig.  It burns, but it calms the nerves.  You ask if they knew the deceased.
  
  'Please do not tell anybody this, but we were secretly involved with each other.  We were going to go public, but we knew that once we did that, the press would never leave us alone.  This was supposed to be our last vacation in secret.'
  
  You give them your condolences.
  
  They continue, 'I should have known it was all wrong as soon as I saw that the colonel was here.  Damn that man.  I don't even think he is a real colonel, just a stupid nickname.  He probably gave it to himself.'
  
  You ask how the colonel and the victim are related.
  
  They laugh, 'Are you serious?  They were brothers.  Everybody knows that.  And everybody knows about their relationship.  They cant stand each other.  But a brother murdering a brother?  Even the colonel isn't that mad.'
  
  With that, they turn back to their drink.
  """)
    billionaire_end()


def billionaire_end():
    answer = input(
        'What would you like to do?  Approach the (argument) or (leave)?')
    if answer == 'argument':
        argument()
    elif answer == 'leave':
        navigate()
    else:
        print('That is not an accepted answer. Please try again.')
        billionaire_end()


def argument():
    print("""You approach the heated conversation.  You instantly hear the name of the deceased, so they obviously both know the victim.  Before the conversation goes any further, both people turn and look at you.
  
  'What the hell do you want?', the colonel says.
  
  'Come on, there is no need to be rude.  Just calm down.', the politician says to the colonel.
  
  Looking at you, they say, 'What can we help you with?  Don't mind us.  Just old friends with old disagreements.  Nothing to worry about.'
  
  'Nothing to worry about!?  My brother is dead and I am going to be the main suspect!', the colonel says looking more and more distraught.
  
  You ask why, and the colonel responds with, 'Because we had a rather loud argument in front of people where I might have alluded to not being very broken up if he suddenly ceased to exist.  I didn't mean it.  We are family.  I never would do anything to hurt family.'  
  
  With this, it seems that the shock of the situation is starting to wear off, and the colonel sits down and starts weeping.
  
  'Perhaps now isn't a great time', the politician says.""")
    argument_end()


def argument_end():
    answer = input(
        'What would you like to do?  Talk to (billionaire) or (leave)')
    if answer == 'billionaire':
        billionaire()
    elif answer == 'leave':
        navigate()
    else:
        print('That is not an accepted answer.  Please try again.')
        argument_end()


def cabin_car():
    print("""You enter the cabin car.  There are six small rooms.  It seems like only two of the rooms have people in them.""")
    cabin_car_end()


def cabin_car_end():
    answer = input('Which door would you like to knock on? (2 / 6) or (leave)')
    if str(answer) == '2':
        widow()
    elif str(answer) == '6':
        butler()
    elif answer == 'leave':
        navigate()
    else:
        print('That is not an accepted answer.  Please try again.')
        cabin_car_end()


def widow():
    print("""You knock on cabin door 2, and you think you can hear sobbing.
  
  The door opens, and there is a woman standing with an urn.  You can tell that they have been crying...a lot.
  
  'Yes?  Can I help you?  Have we almost arrived?  I thought there would be more time.  I'm not ready, yet', she says fighting back tears and gripping the urn tighter.
  
  You realize that this woman is grieving the loss of a loved one and probably has no idea what is happening on this train.
  
  'I'm sorry to have bothered you, my condolences.'
  
  With that, the widow closes the door.""")
    widow_end()


def widow_end():
    answer = input('What would you like to do?  Knock on door (6) or (leave)')
    if str(answer) == '6':
        butler()
    elif answer == 'leave':
        navigate()
    else:
        print('That is not an accepted answer.  Please try again.')
        widow_end()


def butler():
    print("""You knock on door number 6.  This was the room of the deceased.  His Butler slowly opens the door.
  
  'Can I help you?', the butler asks in a snide voice.
  
  You ask if they have any information that could help you guess who the killer was.
  
  'Oh, it could have been any of them.  They all had some sort of relationship with the deceased.'
  
  'For example, take billionaire drowning their sorrows at the bar.  I am sure if you ask, they will tell you how they were in a secret relationship with my now ex-boss, but they won't tell you how they never wanted the press to find out.  Whether that was because they didn't think the relationship serious or for other reasons.  My employer was planning on letting the press know in a few days.'
  
  'Or perhaps it was the colonel, his own brother.  They had a very tumultuous relationship, and I had heard on more than one occasion the colonel threating very unfortunate accidents.'
  
  'It could also be the politician.  My employer was currently funding his rivals campaign.  Oh don't look surprised. Don't tell me you believe that politicians are honest.', with that, the butler starts to chuckle.  You notice, that he winces a bit.""")
    butler_end()


def butler_end():
    answer = input('Would you like to ask the butler if they are ok? (yes/no)')
    if answer == 'yes':
        butler_two_yes()
    elif answer == 'no':
        butler_two_no()
    else:
        print('That is not an acceptable response.  Please try again.')
        butler_end()


def butler_two_no():
    print("""'If there is nothing else, would you please excuse me.  There is much to be done before we arrive.  I also now have the inconvenience of having to find new employment.  Good day.'
  
  The butler closes the door, and you are back in the hallway.""")
    butler_two_end()


def butler_two_end():
    answer = input('What would you like to do?  Knock on door (2) or (leave)')
    if str(answer) == '2':
        widow()
    elif answer == 'leave':
        navigate()
    else:
        print('That is not an accepted response.  Please try again.')
        butler_two_end()


def butler_two_yes():
    print("""'Yes, I am quite fine.  Just slept the wrong way.  These cabins are a bit cramped.'
  
  You notice as they say this, that there is a black and blue just being covered by the sleeve of their shirt.  They see you notice this and pull their sleeve down.
  
  'I assure you that I had no part in what happened today.', they say.
  
  You told them that you didn't think they did, but internally, you find it odd that they said this.
  
  'I think it would be best for you to go now.  I have much to do before we arrive, and now I also have the inconvenience of having to find new employment.' they say, selling the last bit a little too much.  Something is off about this.
  
  You try and extend the conversation, but they aren't having it, and you are now back in the hallway.""")
    butler_two_end()


def conductor():
    print("""'Welcome back!  Would you like to solve the murder?""")
    conductor_end()


def conductor_end():
    answer = input('(yes/no)')
    if answer == 'yes':
        print('Excellent!  So, after all of your sleuthing, who have you decided the murderer was?')
        solve_murder()
    elif answer == 'no':
        print('Ok, come back when you can solve the murder.')
        navigate()
    else:
        print('That is not an acceptable response.  Please try again.')
        conductor_end()


def solve_murder():
    answer = input(
        '(billionaire/butler/colonel/newlyweds/politician/waitress/widow)')
    if answer == 'billionaire':
        print("""'Ah, so you went the Fatal Attraction route.  Nope.  Not this time.'""")
        play_again()
    elif answer == 'butler':
        print('Do you really think the butler did it, or are you just guessing this because the butler usually does it?  ...Well, the butler did do it.  Because the butler always does it.  Congratulations!  You Win!')
        play_again()
    elif answer == 'colonel':
        print('Yeah.  No.')
        play_again()
    elif answer == 'newlyweds':
        print(
            'Did they even realize they were on a train with other people?  Wrong answer.')
        play_again()
    elif answer == 'politician':
        print('This was a really good guess.  Seems plausible.  Not this time, though.')
        play_again()
    elif answer == 'waitress':
        print("Nah.  She just wants the newlyweds to go back to their room so she doesn't have to pretend to be nice anymore.")
        play_again()
    elif answer == 'widow':
        print("Totally the correct answer.  The murder weapon was in the urn.  I'm lying.  This is the most wrong.")
        play_again()
    else:
        print('That is not an acceptable response.  Please try again.')
        solve_murder()


def play_again():
    answer = input('Would you like to play again? (yes/no)')
    if answer == 'yes':
        start_game()
    elif answer == 'no':
        end_game()
    else:
        print('That is not an accepted response.  Please try again.')
        play_again()


def end_game():
    print('Thank you for playing!')


start_game()
