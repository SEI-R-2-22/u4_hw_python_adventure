# Create your own adventure with python here

def build():
    x = input(
        "What life do you want? Mountains, Beaches or live in a van and travel the world?")

    if x == "Van Life":
        x = input('Which Van would you buy? (Benz or Ford)')
        if x == 'Benz':
            x = input('Kind of Van? Tall or Long ')
            if x == 'Long':
                x = input(
                    'Lets edit your van to your liking before traveling the roads! Do you want a kitchen? Yes or No')
                if x == 'No':
                    build()
            else:
                x = input(
                    'How about a griddle in the way back of your van? Yes or No')
                if x == 'No':
                    build()
        else:
            x = input('Do you want a shower in your Van? Yes or No')
            if x == "Yes":
                x = input(
                    'Good Idea! Sink? Yes or No')
                if x == 'Yes':
                    build()
            else:
                x = input(
                    'Plumbing? Yes or No')
                if x == 'Yes':
                    build()
    else:
        x = input("Fold up bed or Fulltime bed?")
        if x == "Fold up bed":
            x = input("Would you like lights installed? or lamps?")
            if x == 'installed':
                x = input(
                    'Yellow lights or White?')
                if x == 'White':
                    build()
            else:
                x = input(
                    'Lamps ars so cute. Are you sure of it in the Van though? Yes or No')
                if x == 'Yes':
                    build()
        else:
            x = input(
                'Would you like desk or no desk to work from home? Or in this case...Work from Van! Ha!')
            if x == "desk":
                x = input(
                    'Would you like an outlet? Yes or No')
                if x == 'Yes':
                    build()
            else:
                x = input(
                    'Would you like a map since you are visiting all 50 States? Yes or No')
                if x == 'Yes':
                    build()
           
                 
    
             again=str(input("Do you want to play again? Yes or No "))
             if again == "no":
             play = False




             # wasnt sure which one was right?
             #def again():
            #if input("Continue? Yes or No") == 'Yes':
         #build()
    #else:
       # exit



          


build()
