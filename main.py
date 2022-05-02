# Create your own adventure with python here
def start_game():

    answer_one = input('Would you like to go on an adventure on the Oregon Trail? (yes/no)')

    if answer_one.lower().strip() == 'yes':

        answer_two = input('You are starting your journey in Houston which direction would you like to go (east/west)').lower().strip()
        if answer_two == 'west': 
            print('You decided to head out towards Oregon')
        else: 
            print('You decided to stay in Houston for now, you will make a decision tomorrow')
        
        answer_three = input('The people in your caravan are hungry, what do you want to do (hunt/pick fruit)').lower().strip()
        if answer_three == 'hunt':
            print('You chose to go hunt buffalo')
        else: 
            print('you chose to go pick fruit')

        answer_four = input('You have been traveling and a wagon wheel breaks do you? (fix it/walk)').lower().strip()
        if answer_four == 'fix it':
            print('You chose wisely and stopped and fixed it')
        else: 
            print('You chose to walk, your journey is gonna take much longer now')

        answer_five = input('you have made it to oregon and you are on the edge of the city do you? (camp here/go in to town)').lower().strip()
        if answer_five == 'go in to town':
            print('Your journey is complete you can now relax')
        else:
            print('You chose to camp outside')
        
        answer_six = input('someone in your caravan get bitten by a rattle snake do you? (stop at the nearest town for medicine/leave them for dead)').lower().strip()
        if answer_six == 'stop at the nearest town for medicine':
            print('You did the right thing and saved their life')
        else:
            print('You lost a member or your caravan and your journey will now be tougher')

        answer_seven = input('you have made it to oregon but you do not like it here do you? (stay/head east to new york)').lower().strip()
        if answer_seven == 'stay':
            print('You are staring new in oregon')
        else:
            print('Your journey continues')
            return start_game()

start_game()

        

