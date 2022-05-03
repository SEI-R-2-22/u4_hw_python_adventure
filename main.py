# Create your own adventure with python here
def start_game():
    print('Masked Individual: Okay..okay, did they sign the waiver? Intercom: Yes. Masked Individual Directely: Wunderbar. Please step into the "Dem Tode Nahe Cryo Chamber" Masked Individual Outspokenly: "To live is to suffer; to survive is to find some meaning in the suffering. Denken Sie daran, dass Sie sterben müussen. *Chamber Seals* ==> Please Select Sex. Male/Female')
    print('Male')
    print('Female')
    
    if answer.lower() == 'Male':
        print('That is the third bottle of whiskey this week, you really are running for your life this time...huh? *Internal: I should have listened...F*ck! I never listen...* The elevator beeps down the hall. You hear the tapping of footsteps nearing your door. Someone is knocking, they are they keep repeating your name. They only want to talk Do you "Open" the door, or "Pretend" to not be home?' )
        print('Open')
        print('Pretend')

    if answer.lower() == 'Open':
        print('You open the door to two men wearing black suits with black glasses. This must be about the debt you owe. Suit 1: "Are you Mr. { REDACTED }? "Yes/No/SlamDoor"')
        print('Yes')
        print('No')
        print('SlamDoor')

    elif answer.lower() == 'Pretend':
        print('The atmosphere grows silent for a moment, there is a loud bang at the door. Then BOOM! The door is kicked off its hinges, the intruders are pissed, this does not end well for you. Would you like to go again?')

    if answer.lower() == 'Yes':
        print('Suit 1: Then you know why we are here. Where is the 400k you owe Mr. { REDACTED }? You: I promise, all I need is more ti--. You meet your demise.. death sealed by a black handgun. I guess they were not here to "just talk". You wake up in the Cryo Chamber. Masked Individual: Willkommen zurück! Would you like to go again?')

    if answer.lower() == 'No':
        print('They glance at each other, then back to you. Suit 2: "Odd... because you sure look like this photo of Mr. { REDACTED }. You are coming with us. We will let Boss determine if you are Mr. { REDACTED } or not. Within an instant, you are knocked unconscious by what looked to be a tire iron. It all happened so fast.. I am as good as dead. You wake up in the Cryo Chamber. Masked Individual: Ouch.. that looked like it hurt. Uh.. so, would you like to go again?')

    elif answer.lower() == 'SlamDoor':
        print('You slam the door and lock it with unbelievable quickness. You hear clicking noise then bullets start shredding through your door. You have no choice but to run through to to your fire escape. You miraculously make it, but got a bullet to the leg. You make it halfway down the fire escape, when you hear your door get kickid in. You should have just enough time to dissapear. Might I suggest skipping town this time? Masked Individual: Tolle! Would you like to go again?')

    elif answer.lower() == 'Female':
        print('At this rate I will pull in over $10,000,000 by end of year. Guess that is just how it goes for the "Greatest Actress" of my generation. There is a knock at the door, you look at you security cameras, you appear to have a fan outside. What do you do? "Pretend" to not be home, or "Answer" the door.')
        print('Pretend')
        print('Answer')

    if answer.lower() == 'Pretend':
        print('The atmosphere grows silent for a moment, there is a loud bang at the door. Then BOOM! The door is kicked off its hinges, the intruder is blabbering about how much they love you, and that they cannot live without you. They say that if they cannot have you, then nobody can. This does not end well for you. Would you like to go again?')

    elif answer.lower() == 'Answer':
        print('You are welcomed by your self-proclaimed, "#1 Fan". They are going on-and-on about how much they love you, and know that the two of you are destined to be together. They are acting kind of.."off", maybe it is just awe, or they are just starstruck. How do you handle the situation? "Entertain" the conversation/  "Ask" to leave/ "SlamDoor" and run? ')
        print('Entertain')
        print('Ask')
        print('SlamDoor')

    if answer.lower() == 'Entertain':
        print('Your #1 Fan rambles about you for the next few hours. You remain attentive to the matter at hand, and even carry on conversation, no matter how uncomfortable you may be. Your fan eventually leaves willingly, on their own accord, but not without telling you how much more they love and appreciate you. #1 Fan: "Thank you for taking the time to speak with me, I love you so much", they exclaim. You seemed to have created a key moment in life. Truly amazing. Would you like to go again?')

    if answer.lower() == 'Ask':
        print('Your #1 Fan appears..hurt..angry. They begin calling you names in a fit of rage. They say you dont deserve their love and attention. They start shouting threats and getting a little to close to you. Eventually, they leave. No harm was done, but you might have lost your #1 Fan for good. Would you like to go again?')

    elif answer.lower() == 'SlamDoor':
        print('You try to slam the door, but it is abruptly blocked by a foot. You turn to run but feel a sharp object pierce your back. #1 Fan: "I told you..if I cannot have you..then no one can". You wake up in the Cryo Chamber. Masked Individual: "Was für ein seltsames Individuum. Very, very, strange. Would you like to go again?"')

def replay_game():
    print('Willkommen zu den Prüfungen! Begin!')
   
    while replay:
        start_game()
        answer = input('Play again? y/n')

        if answer.lower() == 'y':
            replay: True
            print('Thank you, I am finally done with this assignment')