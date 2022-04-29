# Create your own adventure with python here
play = True
endings = {
    1: "\nThe treasure appeared infront of you\n",
    2: "\nA piece of steak appears infront of you\n",
    3: "\nYou found a fish bone\n",
    4: "\nYou reached a dead end\n",
    5: "\nYou found another stone tablet standing with \n\"Pranked\"\n",
    6: "\nYou found a pond of fish\n",
    7: "\nYou are lost forever\n"
}
while play:
    ending = 0
    print(""" You are at the entrance of the maze
  A stone tablet stood infront of you marked with the words
  \"One who shows determination will find what they seek\"\n""")
    input()
    print(" You Entered the maze...")
    input()
    for i in range(1, 7):
        #print(" Path" + str(i) + "\n")
        print("""\n There are two paths infront of you, east and west.
  Which do you choose? (anything other is staying still)""")
        choice = input()
        if choice == "east":
            print(" You went east")
            ending += 1
        elif choice == "west":
            print(" You went west")
            ending += 2
        else:
            print(" You stood still")

    if ending == 6 or ending == 12 or ending == 0:
        print(endings[1])
    elif ending == 7:
        print(endings[2])
    elif ending == 8:
        print(endings[3])
    elif ending == 9:
        print(endings[4])
    elif ending == 10:
        print(endings[5])
    elif ending == 11:
        print(endings[6])
    else:
        print(endings[7])

    print("Play Again? say yes")
    if input() != 'yes':
        play = False
