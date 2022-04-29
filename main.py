# Create your own adventure with python here
you = {
  'name': '',
  'machete': False,
  'banana': True,
  'ending': ''
}
world = {
  'play_count':0,
  'atv':True,
  'glider': True,
  'boat': True
}
derp = "\nSorry, that is not an option. \n"


def printn(str):
  print('\n' + str)

def inputn(str):
  return '\n' + str + ' > '

def play_again(res):
  printn("The end. Congratulations!") if res=='good' else printn("Ouch. The end. Better luck next time.")
  res = input(inputn("Do you want to play again? (Y/N)"))
  start() if res.lower()=='y' else goodbye()

def goodbye():
  printn("You wake with a start. In your bed.")
  printn("Goodbye, " + you['name'] + "!")



##### STORY STARTS HERE #####

def start():
  you['machete'] = False
  world.update({
  'atv':True,
  'glider': True,
  'boat': True
  })
  world['play_count'] += 1

  if you['name']=='':
    you['name'] = input(inputn("What is your name?")) 

  printn("Welcome, " + you['name'])
  chapter1()

def chapter1():
  printn("You wake up with a start on a deserted beach.")
  if you['ending']=='monkey':
    printn("You can't remember what you were dreaming about, but everything sort of smells like fur and bananas.")
  elif you['ending']=='birds':
    printn("You can't remember what you were dreaming about, but there is a ringing in your ears, and everything sort of tastes like feathers.")
  elif you['ending']=='fish':
    printn("You can't remember what you were dreaming about, but a fishy smell hangs in the air.")
  elif you['ending']=='mermaid':
    printn("You can't remember what you were dreaming about, but your legs feel weird and unnatural.")
  elif you['ending']=='wizard':
    printn("You can't remember what you were dreaming about, but you think you smell smoke.")
  # elif you['ending']=='birds':
  # elif you['ending']=='fish':
  # elif you['ending']=='wizard':
  beach()

def beach():
  printn("The sand is soft under your toes. Nearby is a small boat worthy of travel on the SEA. Further along the BEACH, there is something large that you cannot quite see. Behind you, there is a path into the JUNGLE, and beyond, a cliff.")
  res = input(inputn("Which way do you go?"))

  if res.upper()=='SEA':
    sea_part1()
  elif res.upper()=='BEACH':
    beach_part2()
  elif res.upper()=='JUNGLE':
    jungle_part1()
  else:
    printn(derp)
    chapter1()

def beach_part2():
  printn("Walking along the beach, you come upon... an ATV! Sweet!")
  res = input(inputn("Do you go BACK like a lame-o? Or you do go explore on the ATV?"))
  if res.lower()=='back':
    printn("Really? Okay, I guess, if you hate fun...")
    beach()
  elif res.lower()=='atv':
    printn("You zoom off down the beach, sand spraying behind you like a cloud. Up ahead, you see the mouth of a CAVE... and a fallen tree that looks enticingly like a RAMP.")
    res = input(inputn("Where you gonna drive?"))
    if res.lower()=='ramp':
      printn("You open the throttle and bee-line towards the ramp. You hit it perfectly at top speed, and for a moment, you are soaring through the air like every car chase in every movie ever. It's majestic.")
      printn("...And then, predictably, gravity wins and the ATV  plummets to earth. Without you. What?")
      printn("You feel a pinch on your shoulders, and look up to see that you are caught in the talons of the largest bird you've ever seen. You have a sinking feeling as you fly up towards a flock of these huge birds nesting under the cliffs. Uh oh.")
      bird_food()
    elif res.lower()=='cave':
      printn("The cave quickly becomes to narrow for your new ride, but you see a glowing light at the end of the tunnel, so you park it and walk deeper into the cave.")
      printn("As you approach, you see a silouette against the light. Without turning, a deep voice says,")
      wizard()

def wizard():      
  res = input(inputn("'Welcome, " + you['name'] + ". I've been watching you with great interest for some time. You are trapped here, whether you know it or not. Are you ready to be free? (Y/N)"))

  if res.lower()=='yes' or 'y':
    printn("The figure turns, places a hand on your head, and says quietly, 'Too bad, this is way more fun than what's waiting for you back home.'")
    goodbye()
  elif res.lower()=='no' or 'n':
    printn("'Really?' He seems surprised. 'Well. Um, Okay then. Back you go.'")
    printn("There is a puff of smoke, and everything goes black.")
    start()
  else:
    printn(derp)
    wizard()

def sea_part1(): ###########################
  printn("The waters are calm as you paddle into the sea. A little ways off, you see a small ISLAND. You also think you can see something way out on the HORIZON.")
  res = input(inputn("Where do you go?"))

  if res.lower()=='island':
    island()
  elif res.lower()=='horizon':
    printn("You can't tell, but you don't seem to be making any progress.")
    sea_part1()
  else:
    printn(derp)
    sea_part1()

def island():
  printn("As you approach the island, you notice it is guarded by mermen and mermaids with tridents and other weapons. You start to turn your boat around, but a hand comes out of the water and grabs the edge, stopping you in your tracks.")
  printn("A merman emerges from the water and says, 'Are you the one they call "+ you['name'] + "? We have heard of your coming.")
  res = input(inputn("Do you wish to join us? (Y/N)"))
  if res.lower()=='y' or res.lower()=='yes':
    printn("You begin to feel warm magic cover you like a blanket, and then your legs begin to feel heavy. When you look down, you've grown a tail! You dive into the water, and it feels amazing!")
    you['ending'] = 'mermaid'
    play_again('good')
  elif res.lower()=='n' or res.lower()=='no':
    printn("'As you wish,' says the great creature. A strong wind suddenly blows, and you find yourself sailing swiftly back to shore. The boat carves a path up onto the beach, and you climb out.")
    beach()
  else:
    printn(derp)
    island()
 




def jungle_part1():
  if not you['machete']: 
    printn("After walking a ways, you find yourself at a fork. You see a MACHETE embedded in a rotted stump. To the RIGHT, the path winds further up towards the cliff. To the LEFT, another path is narrow and overgrown. In front of you, delicious BANANAS hang from a tree.")

  elif you['machete']:
    printn('You stand at the fork in the path. To the RIGHT, the path winds further up towards the cliff. To the LEFT, another path is narrow and overgrown. In front of you, delicious BANANAS hang from a tree.')

  res = input(inputn("What do you do?"))
  
  if res.lower()=='machete':
    you['machete'] = True
    printn('You take the machete.')
    jungle_part1()

  elif res.lower()=='left' and you['machete']:
    printn("Channeling your inner Dwayne Johnson from 'Jumanji', you hack your way through the jungle.")
    jungle_left()

  elif res.lower()=='left' and not you['machete']:
    printn('The path is far too overgrown, although it does look enticing...')
    jungle_part1() #repeat

  elif res.lower()=='right':
    printn("You climb up the path and come out upon a lovely cliff overlooking the sea.")
    cliff_part1()

  elif res.lower()=='bananas':
    banana_part1()

  else:
    printn(derp)
    jungle_part1()



def banana_part1():
  printn("You grab a banana, but before you can peel it, a monkey zips down from the tree, stares you right in the eyes, and grabs the banana! Cheeky monkey!")
  printn("He runs off into the jungle.")
  res = input(inputn("Do you CHASE, or do you STAY?"))
  if res.lower()=='stay':
    printn("You watch it run off into the jungle. Oh well.")
    jungle_part1()
  elif res.lower()=='chase':
    printn("Damn dirty ape! You chase after him, deeper into the jungle.")
    jungle_left()


  
def jungle_left():  #############################
  printn("You stumble suddenly into a dark clearing. Huge monkeys step out of the shadows, baring their teeth and looking generally unfriendly.")
  res = input(inputn("Do you STAND your ground, or do you RUN?"))

  if res.lower()=='stand':
    printn("Not sure what you expected here. The monkeys surround you, teeth bared. They crowd closer and closer...")
    monkey_bad_ending()
  elif res.lower()=='run':
    printn("You make a run for it. You're pretty fast... but the monkeys are faster.")
    monkey_bad_ending()
  elif res.lower()=='machete' and you['machete']:
    monkey_good_ending()
  else:
    printn(derp)
    jungle_left()


def monkey_bad_ending():
  printn("You feel a heavy 'thud' on the back of your skull, and the world goes black. The rest is too gruesome to report, but if you need a visual, go watch the beginning of the movie 'Congo'.")
  you['ending'] = 'monkey'
  play_again('bad')

def monkey_good_ending():
  printn("OF COURSE! YOU HAVE A MACHETE! Brandishing your machete, you charge into clearing at the largest monkey in the pack. To your surprise, he kneels at your feet!")
  printn("'You must be the mighty " + you['name'] + " that was fortold to us! Hail, mighty " + you['name'] + "!")
  printn("The monkeys begin to chant your name, and a crown of gold is placed upon your head. You are now the monkey king!")
  you['ending']='monkey'
  play_again('good')






def cliff_part1(): ##################
  printn("You hear birds caw-cawing just out of sight over the cliff's edge, which you might be able to see if you LOOK over. The water below looks so calm and clear you could DIVE in and barely make a splash.")
  if world['glider']:
    printn("Out of the corner of your eye, you spy what looks like a GLIDER tucked out of sight under some bushes.")
  
  res_str = "Do you LOOK for the birds, or DIVE into the sea"
  res_str += ", or take the GLIDER" if world['glider'] else ""
  res_str += "?"
  res = input(inputn(res_str))

  if res.lower()=='look':
    look()
  elif res.lower()=='dive':
    dive()
  elif res.lower()=='glider':
    glider()
  else:
    printn(derp)
    cliff_part1

def look():
  printn("You peer over the edge to see gigantic birds nesting on the cliffs. As you pull back in surprise, the cliff crumbles and you slip over the edge. You fall and fall and fall...")
  printn("...and suddenly, you're flying! You find yourself on the back of a great sea eagle, who turns and says, 'Greetings, " + you['name'] + ". We have been expecting you.")
  printn("You fly on the back of the great bird, and the wind whips through your hair. This is basically the greatest thing, ever. You and your new giant sea eagle fly off over the horizon to start a great adventure.")
  you['ending']='birds'
  play_again('good')

def dive():
  printn("You take a running start and execute a perfect arching swan dive over the cliff's edge. You speed gracefully towards the water and cut smoothly through the surface. So worth it!")
  printn("It's about then you notice the piranhas.")
  piranhas()

def glider():
  printn("The glider feels light in your hands, and with barely any effor at all, you slip over the cliff's edge and soar into the air. YOu're off!")
  printn("In the distance you spot a small ISLAND, but it's quite far away. Below you, the BEACH looks warm.")
  res = input(inputn("Do you head for the ISLAND, the BEACH, or go back to the CLIFF?"))
  if res.lower()=='beach':
    world['glider']=False
    printn("You soar down to the beach, but the landing is a bit bumpy. You're fine, but the glider is smashed to bits. Bummer. Anyway, you're back on the beach!")
    beach()
  elif res.lower()=='island':
    print("You soar out towards the island. What a great view! Sadly, the island is much further than you thought, and you're losing altitude fast. With a sinking feeling, you glide gently but with finality into the water.")
    piranhas()
  elif res.lower()=='cliff':
    printn("Thinking to head back towards safety, you turn around and steer back towards the cliff. As you approach, however, you notice the birds nesting along the cliffs are much larger than you thought. And they don't seem thrilled to see you.")
    bird_food()
  else:
    printn(derp)
    glider()

def bird_food():
  printn("The birds take flight and swarm around you. There are feathers everywhere. Hitchcock would be proud.")
  you['ending']='birds'
  play_again('bad')
    


def piranhas():
  printn("The nasty little fish swarm around you, until the water is positively churning. At least you're helping keep the food chain going.")
  you['ending']='fish'
  play_again('bad')




### BEGIN THE ADVENTURE
start()