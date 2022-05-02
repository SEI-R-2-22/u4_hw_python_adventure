# Create your own adventure with python here
answer = input("Ready for an adventure? (yes/no)")

if answer.lower().strip() == "yes":

    answer = input(
        "Two roads diverged in a yellow wood. And sorry you could not travel both; would you choose the one: a. less traveled or b. heavily trodden way?")

    if answer.lower().strip() == "a":
        answer = input("You chose the road with the better claim and happen upon a Ranger, Elf, and a Dwarf. Do you: a. kindly ask them their buisness in the woods, b. ask them why they're in your woods, c. try to sneak away?")

        if answer.lower().strip() == "a":
            asnwer = input("The Ranger tells you they are looking for their three hobbit friends. They ask if you'd care to join in and help. Do you: a. reply with 'Sounds like a fun adventure', b. reply 'Sounds like you need more help than I can give', c. give them a blank stare")

            if answer.lower().strip() == "a":
                print("You join their company and travel through the forest. The four of you come upon a wizard robed in white. Frozen by some magical spell cast by the wizard you begin to tremble in fear. Come to find out the wizard is great friends with the Ranger, Dwarf, and the Elf. You continue on until you battle with Orcs and Saruman. The Ents come to your aid. Low and behold the hobbits your company was searching for come riding on the shoulders of the Ents. What an adventure. THE END")

            elif answer.lower().strip() == "b":
                print("They ask that you be on the lookout for the two tiny beings. And mumble something about how it's not safe to be in these woods alone. You ignore the rest of what they say and continue your adventure. Only to find yourself lost and nightfall fast approaching. You decide to build a fire for some warmth. Well, that was a bad decision because you attracted the attention of a horde of Orcs who haven't had meat to eat in a long time. All said and done, you were a tasty treat easily bagged. THE END")

            else:
                answer = input("The Dwarf tells you it's not polite to stare. The Elf tells the Dwarf you've probably never seen such a hideous sight as him. Flustered the Dwarf huffs and puffs. The Ranger strongly suggest you come with them as it will be night soon and these woods aren't too kind to lone travelers. Do you: a. tag a long, b. tell them you're going back the way you came?")

                if answer.lower().strip() == "a":
                    print("You join their company and travel through the forest. The four of you come upon a wizard robed in white. Frozen by some magical spell cast by the wizard you begin to tremble in fear. Come to find out the wizard is great friends with the Ranger, Dwarf, and the Elf. You continue on until you battle with Orcs and Saruman. The Ents come to your aid. Low and behold the hobbits your company was searching for come riding on the shoulders of the Ents. What an adventure. THE END")

                else:
                    print("You're lucky enough to find your way back to the fork and make it back to the inn you were staying at before nightfall. In the night you awake from your slumber to hear a bunch of commotion in the far off distance. You wake in the morning and head to the tavern below your room. The room is filled with the bustle of many chipper Rowhanians all talking about the fall of Saruman's Tower. Sounds like that would have been a fun adventure to have gone on! THE END")

        elif answer.lower().strip() == "b":
            answer = input("The dwarf doesn't quite like your tone. 'These woods belong to the Ent's and you don't look much like an Ent. Who do you serve?!' he ask you. Do you asnwer with: a. give a befuddled look, b. Sauron!, c. I have no master")

            if answer.lower().strip() == "a":
                answer = input("'You look too harmless. This one must be a relative of our Hobbit friends,' says the Dwarf. 'I don't think you mean to be in these woods. Come with us but watch your tongue or you'll have to deal with more than the likes of us three!' Exclaims the Elf. ")

            elif answer.lower().strip() == "b":
                print("That was a rather poor choice! All three draw their weapons and dispatch you. Left a cold corpse with no story to tell. THE END")

            else:
                answer = input("'Then choose this day! Stand with us or give allgeiance with those that bear the White Hand! Exlaims the Dwarf. Do you: a. side with the three companions, or b. side with whoever they were on about?")

                if answer.lower().strip() == "a":
                    print("You join their company and travel through the forest. The four of you come upon a wizard robed in white. Frozen by some magical spell cast by the wizard you begin to tremble in fear. Come to find out the wizard is great friends with the Ranger, Dwarf, and the Elf. You continue on until you battle with Orcs and Saruman. The Ents come to your aid. Low and behold the hobbits your company was searching for come riding on the shoulders of the Ents. What an adventure. THE END")

                else:
                    print("That was a rather poor choice! All three draw their weapons and dispatch you. Left a cold corpse with no story to tell. THE END")

        else:
            answer = input("The elf hears you trying to sneak away and you find an arrow through your shirt nailing you to a tree. 'Who sent you the elf ask?' How do you answer: a. I was just walking through the woods. I'm here on my own accord. b. I demand you let me go. c. You stumble over your words and manage to blurt out a name they've never heard")

            if answer.lower().strip() == "a":
                print("'You look like a spy to us! You shall not go through these woods freely,' says the Elf. They bound you with rope to secure you and bring you along with them. Not shortly after you and the three are bombarded by a horde of Orcs. They do little to protect you seeing as how they think you are a spy for them. You wind up being taken by the Orcs and becoming a meal for them! THE END")

            elif answer.lower().strip() == "b":
                print("'Let your lord come a free you, you spy!' shouts the Elf. They bound you to the tree and leave you for any passer by that may happen upon you. And not long after the Nazgul come by and consume your soul. THE END")

            else:
                print("'We are unfamiliar with the name,' says the Elf. 'Perhaps you should come with us. In the meantime you can tell us all about this character.' You saddle up with the Dwarf and ride with them until nightfall. You and the three bed down for the night. You wake to the sound of clanking swords and arrows whirling through the air. A troop of trolls came upon your camp early in the morning. The three companions forgot you were with them and soon you find they are gone. You're left there to fend for yourself. Not a good situation to be in as you have no clue where you are. You bumble around to gather your bearings but stumble over a clif and into a ravine. With a broken leg you won't be much for getting yourself found. A pack of wolves finds you an easy meal. THE END")

    elif answer.lower().strip() == "b":
        answer = input("You chose the way many have traveled before you. Seems like a safe choice. But you shortly come upon a group of Trolls! Do you: a. run up and fight them all, b. try to sneak around")

        if answer.lower().strip() == "a":
            print(
                "What an ill desicion that was. The trolls make a nice little snack out of you. THE END")

        elif answer.lower().strip() == "b":
            answer = input("You barely make it out of there without the trolls realizing you were there. You happen upon three companions. A Ranger, a Dwarf, and an Elf. Do you: a. kindly ask them their buisness in the woods, b. tell them about the trolls?")

            if answer.lower().strip() == "a":
                print("They tell you about their lost companions. You tell them you'd be glad to help look for them. You join their company and travel through the forest. The four of you come upon a wizard robed in white. Frozen by some magical spell cast by the wizard you begin to tremble in fear. Come to find out the wizard is great friends with the Ranger, Dwarf, and the Elf. You continue on until you battle with Orcs and Saruman. The Ents come to your aid. Low and behold the hobbits your company was searching for come riding on the shoulders of the Ents. What an adventure. THE END")

            else:
                answer = input("They tell you not to worry much. Trolls aren't too keen on smelling past their own odor. You'll be safe if you stick with them. Do you: a. stick with the three companions, or b. go your own way?")
                if answer.lower().strip() == "a":
                    print("You join their company and travel through the forest. The four of you come upon a wizard robed in white. Frozen by some magical spell cast by the wizard you begin to tremble in fear. Come to find out the wizard is great friends with the Ranger, Dwarf, and the Elf. You continue on until you battle with Orcs and Saruman. The Ents come to your aid. Low and behold the hobbits your company was searching for come riding on the shoulders of the Ents. What an adventure. THE END")
                else:
                    print("That was unwise. You run into the trolls again because you don't know your way around these woods and become a tasty little snack for them. THE END")

    else:
        print("Wrong choice! Better luck next time.")

else:
    print("Come back when you are!")
