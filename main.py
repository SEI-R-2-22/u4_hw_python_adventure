# Create your own adventure with python here
def game():
    answer = input(
        'Hi Cady Heron! Your family has chosen to move back to the United States from Africa. You have the choice to go to public high school or be home schooled, what is your choice? (public/home)')

    if answer.lower().strip() == 'public':

        answer = input(
            'Today is your first day of high school! Your biggest decision in the morning is picking an outfit. You can wear pink, green, black, blue. Which will you go with? (pink/green/black/blue)').lower().strip()
        if answer == 'black':
            answer = input('Janis and Damien see you strolling through the hallway looking for your class. They offer to help you find the room. Do you take their help? (yes/no)')
            if answer == 'yes':
                print('They actually have the class first period class as you! Both of them tell you about the most popular clique called the Plastics and their horror stories. After listening to that you steer clear of the Plastics and enjoy the company of your two new friends.')
            else:
                print('It can not be that hard to find this class! After all you are Cady Heron, a literal genius. You find your class after searching but end up being 15 mins late. Janis and Damien are in the same class so it is a little awkward. They do not become your friends.')
                return game()

        elif answer == 'green':
            answer = input(
                'While searching for your first period class a girl named Karen walks up to you. She says you look lost and offers you help. Do you take it? (yes/no)').lower().strip()
            if answer == 'yes':
                print('Karen looks at your schedule, blankly looks at you and says what is calculus 1? She is no help, you miss your first class and fail calculus.')
            else:
                print('Karen seems more lost than you are! You can do this on your own! You find your class just in time as it begins. You also meet two classmates Janis and Damien who become your lifelong friends.')
                return game()

        elif answer == 'blue':
            answer = input(
                'You are feeling a little lost looking for your first period class when Gretchen comes up to you. She loves your outfit and mentioned that blue is an under rated color. Do you want to ask her for help in finding your class? (yes/no)').lower().strip()
            if answer == 'yes':
                print("Gretchen helps you find your class. She invites you to each lunch with the Plastics that afternoon. At lunch you meet Regina and Karen and become apart of the clique. They stress you out with their drama.")
            else:
                print('You thank Gretchen for the compliment but you can find the class on your own! You find it just in time. You also meet two classmates Janis and Damien who become your lifelong friends')
                return game()

        elif answer == 'pink':
            answer = input(
                'You are beginning to feel overwhelmed and lost when Regina comes up to you. She gives you a back handed compliment that your beautiful pink oufit would look much better on her. You awkwardly laugh. She invites you to join her for lunch. What do you say? (yes/no)').lower().strip()
            if answer == 'yes':
                print('Regina is not one to help anyone find their class, so you end up missing it all together! At lunch she tells you calculus are for non-Plastics anyways. You become her bff and her constant drama drives you insane. You are forced to keep track of it all in the infamous burn book.')
            else:
                print("Ouch! That backhanded compliment hurt. You'd rather not go to lunch with someone like that. You find your calculus class and meet Janis and Damien!")
                return game()

    else: 
        print('You decided to be home schooled! You learned at your own pace and excelled in calculus. You were offered a full ride to Harvard. Congradulations! ')
       
game()