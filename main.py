def intro():
  name = input('What is your name? ')
  start_game = input(f'Hello {name}, do you want to play a game? (Type Y or N): ').lower()
  if start_game == 'Y':
    print("Okay, let's set off on our adventure!")
    game()
  else:
    print("That's too bad, start the program again whenever you are ready!")

def game():
  scene1 = input('Where would you like to go on our adventure? (Choices are Europe, Asia, South America, or the United States): ').lower()

  my_dict = {}
  if scene1 in 'europe':
    scene1='europe'
    my_dict = { 
      'country1': 'london, england',
      'food1':'tea & scones',
      'sight1':'big ben',
      'country2': 'paris, france',
      'food2':'croissants',
      'sight2':'the eiffel tower',
      'country3': 'rome, italy', 
      'food3':'pasta',
      'sight3':'the colosseum',
      }
  elif scene1 in 'asia':
    scene1='asia'
    my_dict = {
      'country1': 'shanghai, china',
      'food1': 'steamed crab',
      'sight1': 'the yuyuan gardens',
      'country2': 'mumbai, india',
      'food2':'baida roti',
      'sight2':'the kanheri caves',
      'country3': 'tokyo, japan',
      'food3':'sushi',
      'sight3':'the cherry blossom groves',
      }
  elif scene1 in 'south america':
    scene1='south america'
    my_dict = {
      'country1': 'lima, peru',
      'food1': 'ceviche',
      'sight1': 'the peruvian catacombs',
      'country2': 'buenos aires, argentina',
      'food2':'croissants',
      'sight2':'the teatro colón opera house',
      'country3': 'santiago, chile',
      'food3':'completos, chilean hot dogs',
      'sight3':'skiing in the andes',
    }
  elif scene1 in 'united states' or scene1 == 'us':
    scene1='the united states'
    my_dict = {
      'country1': 'atlanta, georgia',
      'food1': 'barbecue',
      'sight1': 'the coke factory',
      'country2': 'chicago, illinois',
      'food2':'pizza',
      'sight2':'the adler planetarium',
      'country3': 'new york, new york',
      'food3':'pizza',
      'sight3':'times square',
    }
  else:
    print("I'm sorry!That was not one of the options. Please try the game again with a correct input")

  scene2 = input(f"That's my favorite place to go too! Where in {scene1.title()} do you want to travel to? (Choices are \n-{my_dict['country1'].title()} \n-{my_dict['country2'].title()} \n-{my_dict['country3'].title()})\n\nYour Answer: ").lower()

  if (scene2 in my_dict['country1']):
    my_country=my_dict['country1']
  elif (scene2 in my_dict['country2']):
    my_country=my_dict['country2']
  elif (scene2 in my_dict['country3']):
    my_country=my_dict['country3']
  else:
    print('wrong')

  step1 = 'eat the local food'
  step2 = 'explore the city'

  scene3 = input(f"I've been to lots of parts of {scene1.title()}, but never {my_country.title()}. What do you want to do there? (Choices are \n-{step1.title()} \n-{step2.title()})\n\nYour Answer: ").lower()

  if (scene3 in step1) and (scene2 in my_dict['country1']):
    scene2=my_dict['country1'].title()
    print(f"Oh, if you like food, don't leave there without getting some {my_dict['food1']}")
  elif (scene3 in step2) and (scene2 in my_dict['country1']):
    print(f"There is never enough time to see all the sites, but don't leave there until you've gone to {my_dict['sight1']}")

  elif (scene3 in step1) and (scene2 in my_dict['country2']):
    scene2=my_dict['country2'].title()
    print(f"Oh, if you like food, don't leave there without getting some {my_dict['food2']}")
  elif (scene3 in step2) and (scene2 in my_dict['country2']):
    print(f"There is never enough time to see all the sites, but don't leave there until you've gone to {my_dict['sight2']}")

  elif (scene3 in step1) and (scene2 in my_dict['country3']):
    scene2=my_dict['country3'].title()
    print(f"Oh, if you like food, don't leave there without getting some {my_dict['food3']}")
  elif (scene3 in step2) and (scene2 in my_dict['country3']):
    print(f"There is never enough time to see all the sites, but don't leave there until you've gone to {my_dict['sight3']}")
  else: 
    print("I'm sorry!That was not one of the options. Please try the game again with a correct input")

def resetGame():
  reset = input('Would you like to play again? Choices:\n-Yes,\n-No)\n\nYour Answer: ').lower()
  if reset in 'yes':
    game()
  else:
    print("That's okay! I have to catch a plane to the Esperanza station on Antartica soon anyway. I'll see you around!")

intro()
game()
resetGame()