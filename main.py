# Create your own adventure with python here
def embark():
    print("You're embarking on the magical journey of aging! It's your birthday, and we're planning a party.")
    age = input("How old are you?")
    numeric_age = int(age)

    if numeric_age < 2:
        print("You're just an infant!")
        flavor = input(
            "It's time to bake your very first birthday cake! Do you prefer rice pudding (R), mashed peas (P), or chocolate (C) filling?")
        while flavor != "R" and flavor != "P" and flavor != "C":
            flavor = input(
                "Please enter the appropriate letter (R, P, or C) to choose the flavor of your cake!")

        if flavor == "R":
            print(
                "Yuck, rice pudding! Head to the grocery store to buy some jars of Gerber baby food.")
        elif flavor == "P":
            peas_preference = input(
                "Ew, mashed peas! Do you prefer regular homegrown peas (R) or sugarsnap peas (S)?")
            if peas_preference == 'R':
                print("Head to your backyard garden to harvest some homegrown peas!")
            elif peas_preference == 'S':
                print("Head to your local farm's vegetable patch!")
            else:
                print("That option is not available")
        elif flavor == 'C':
            chocolate_choice = input(
                "Do you prefer milk chocolate (M) or dark chocolate (D)?")
            if chocolate_choice == 'M':
                print("Ok, buy some sweet Hershey's chocolate for the cake!")
            elif chocolate_choice == 'D':
                print("Ok, buy some bittersweet Godiva chocolate for the cake!")
            else:
                print("That option is not available")
        else:
            print("Could not find that cake flavor. Let's go with a plain spongecake.")
    elif numeric_age < 5:
        print("You are a tantrum-throwing toddler!")
        party_favor = input(
            "It's time to pick party favors for your guests. Do you prefer toys (T) or books (B)?")
        while party_favor != 'T' and party_favor != 'B':
            party_favor = input("Please type T for toys or B for books.")
        if party_favor == 'T':
            toy_choice = input(
                "Do you like building blocks (BB) or Barbie dolls (BD)?")
            if toy_choice == 'BB':
                print(
                    "As a destructive toddler, you knocked over the tower of blocks in the toy store and broke them all.")
            elif toy_choice == 'BD':
                print("You gave your Barbie doll an unsightly haircut.")
            else:
                print("Could not find that toy")
        else:
            book_choice = input(
                "Do you prefer to read The Canterbury Tales (C) or Paddington (P)?")
            if book_choice == 'C':
                print("Unfortunately, you are too young for Chaucer.")
            elif book_choice == 'P':
                print("A childhood classic!")
            else:
                print("Could not find that book")
    elif numeric_age > 13 and numeric_age < 20:
        print("You are a teenager!")
        activity = input(
            "It's time to pick an activity for your guests. Do you prefer going to a movie (M) or out to dinner (D)?")
        if activity == 'M':
            movie_choice = input("Do you prefer Titanic or Elf?")
            if movie_choice == "Titanic":
                print(
                    "That is too sad for a birthday party. All of your guests will leave!")
            elif movie_choice == 'Elf':
                print(
                    "Elf is the perfect comedy for birthday parties and the holiday season!")
            else:
                print("Could not find that movie")
        elif activity == 'D':
            dinner_choice = input(
                "Do you prefer deli (D) or delicious Italian fare (I)?")
            if dinner_choice == 'D':
                print("Corned beef and pickles it is!")
            elif dinner_choice == 'I':
                print("Ravioli and chicken parmesan it is!")
            else:
                print("Could not find that food")
        else:
            print("Could not organize that activity")
    elif numeric_age > 20:
        print("You're an adult!")
        charity = input(
            "You're too old for a birthday party. Spend time volunteering at your local animal shelter instead. Do you want to work with cats (C) or dogs (D)?")
        if charity == 'C':
            cat_activity = input(
                "Do you want to feed cats (F) or groom (G) cats?")
            if cat_activity == 'F':
                print("Buy cans of cat food for the rescue cats")
            elif cat_activity == 'G':
                print("Buy a cat brush to comb their fur")
            else:
                print("Choose a different charitable deed")
        elif charity == 'D':
            dog_activity = input(
                "Do you want to walk dogs (W) or feed dogs (F)?")
            if dog_activity == 'W':
                print("Prepare the dog harness and leash")
            elif dog_activity == 'F':
                print("Prepare some bags of kibble")
            else:
                print("Choose a different charitable deed")
        else:
            print("Animal shelter not found")
    else:
        print("Whoops, your birthday party plans fell through!")


embark()
start_over = input('Would you like to play again? Y/N')
if start_over == 'Y':
    embark()
else:
    print('Thanks for playing. Bye for now!')
