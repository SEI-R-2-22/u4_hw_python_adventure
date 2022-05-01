# Create your own adventure with python here

def play():
    tape = input(
        "A tape arrived in the mail for You get a tape in the mail? Do you watch it or no?")
    
    if tape == "yes":
        tape1 = input("You pop in the tape in and hear your name being called from it. Do you continue to watch?")
        if tape1 == "yes":
           tape2 = input("You cant tell if the tape is old and fuzzy or if its completely busted. Do you still watch")
           if tape2 == "yes":
               tape3 = input("You start to see images building on the screen they're ominious and maybe it's a face? Continue? ")
               if tape3 == "yes":
                   print("BOO! Your soul is taken!")
               else:
                   print("Man screw VHS this is weird.")
           if tape2 == "no":
               tapeI = input("IDK man you've been feeling real weird since you tried watching this tape. Maybe we should try throwing it away.")
               if tapeI == "yes":
                   print("this is probably for the best. That ish is weird")
               elif tapeI == "lets send it to someone else":
                   input("You stamp the video and pick some John Doe. Lets not think about this. ok?")
                   print(" a few days later on the news you see John Doe died mysteriously")
               else:
                   print("You know it will come back for you") 

        elif tape1 == "no":
            input("It was calling your name? lets stop and put it on a shelf")
            tapeII = input("You can still hear the tapes voice calling your name maybe you should give it a watch again")  
            if tapeII == "yes":
                tapeIII = input("Its back in the tape deck and you start to see the movie come together more. Continue?")
                if tapeIII == "yes":
                    print("Bahaha You dead")
                else:
                    print("it still haunts you but you know something is wrong and you shouldnt watch it" )
            else:
                tapeI    

    else:
         tapeA = input("You dont have friends, who would send this lets investigate?")
         if tapeA == "yes":
           tapeB = input("You find out its from an occult, do you continue")
           if tapeB == "yes":
               tape3 = input("Well now youre apart of them, and you send the tape out to unsuspecting people are you ok with this ?")
               if tape3 == "yes":
                   print("Well they would have taken your soul anyways, whatever.")
               else:
                   print("Your soul is mine anyhow")
           else: 
               print("they gonna get you regardless but run")
         else:
             print("Lets just try and survive today") 
play()