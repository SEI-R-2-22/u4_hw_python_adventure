# Create your own adventure with python here

def ask_name():
    name = input('Hi Adventure, before we begin, What is your name: ')
    return name


def fillers():
    input('press enter to continue...\n')


def begin_game(name):
    res = input(
        name + ", " + 'are you ready to begin? press yes(y)/no(n) \n')
    if(res.upper() == 'Y'):
        res = "YES"
    return str(res.upper())


def ask_begin_again(name):
    res = input(name + ", " + "press yes(y) to begin when ready. \n")
    if(res.upper() == 'Y'):
        res = "YES"
    return res


def question1():
    res = input("Are you interested in Front-end development, or Back-end developement?\n Press 1 for Front-end or \n Press 2 for Back-end. \n")

    if res == '1' or res == '2':
        return res
    else:
        print('try again: \n')
        question1()


def question2(answer1):
    if answer1 == '1':
        res = input("Front-end it is. Do you like to make things look pretty or building features?\n Press 1 for pretty things or press 2 for building features. \n")
        if res == '1' or res == '2':
            return res
        else:
            print('try again:\n')
            question2(answer1)

    else:
        res2 = input(
            "Back-end!!!!. Do you like to work with server request or database?\n Press 3 for server request or Press 4 for database. \n")
        if res2 == '3' or res2 == '4':
            return res2
        else:
            question2(answer1)


def question3(answer2):
    if answer2 == '1':
        res = input("Making things pretty in the front-end, we have these lauguage, which would you like to learn: \nPress 1 for CSS, 2 for HTML, and 3 for both.\n ")
        if res == '1' or res == '2' or res == '3':
            return res
        else:
            question3(answer2)
    elif answer2 == '2' or answer2 == '3':
        res2 = input(
            "lookings like you building features. We have 2 options for you. \n We have React and VUE. \nPress 4 for React, and 5 for Vue\n")
        if res2 == '4' or res2 == '5':
            return res2
        else:
            question3(answer2)
    else:
        res3 = input("Looks like you like tables, We have MongoDB and PostgreSQL for you. Which would you like to learn?\n Press 6 for MongoDB, 7 for PostgresSQL or 8 for both. \n")
        if res3 == '6' or res3 == '7' or res3 == '8':
            return res3
        else:
            question3(answer2)


def question4(answer3):

    if answer3 == '1':
        res = input(
            'I see you selected CSS. Go here to learn https://www.w3schools.com/w3css/.\n Press 1 to end. press 2 to restart questionnair.\n ')
        if res == '1' or res == '2':
            return res
        else:
            question4(answer3)
    elif answer3 == '2':
        res2 = input(
            'I see you selected HTML. Go here to learn https://www.w3schools.com/html/default.asp.\n Press 1 to end. press 2 to restart questionnair. \n')
        if res2 == '1' or res2 == '2':
            return res2
        else:
            question4(answer3)
    elif answer3 == '3':
        res3 = input(
            'I see you selected both. Go here to learn https://www.w3schools.com/.\n Press 1 to end. press 2 to restart questionnair. \n')
        if res3 == '1' or res3 == '2':
            return res3
        else:
            question4(answer3)
    elif answer3 == '4':
        res4 = input(
            'I see you selected React. Go here to learn https://www.w3schools.com/REACT/DEFAULT.ASP.\n Press 1 to end. press 2 to restart questionnair. \n')
        if res4 == '1' or res4 == '2':
            return res4
        else:
            question4(answer3)
    elif answer3 == '5':
        res5 = input(
            'I see you selected Vue. Go here to learn https://vuejs.org/.\n Press 1 to end. press 2 to restart questionnair. \n')
        if res5 == '1' or res5 == '2':
            return res5
        else:
            question4(answer3)
    elif answer3 == '6':
        res6 = input(
            'I see you selected MongoDB. Go here to learn www.mongodb.com\n Press 1 to end. press 2 to restart questionnair. \n')
        if res6 == '1' or res6 == '2':
            return res6
        else:
            question4(answer3)
    elif answer3 == '7':
        res7 = input(
            'I see you selected PostgreSQL. Go here to learn www.postgresql.org\n Press 1 to end. press 2 to restart questionnair. \n')
        if res7 == '1' or res7 == '2':
            return res7
        else:
            question4(answer3)
    elif answer3 == '8':
        res8 = input(
            'I see you selected PostgreSQL. Go here to learn www.mongodb.com and www.postgresql.org\n Press 1 to end. press 2 to restart questionnair. \n')
        if res8 == '1' or res8 == '2':
            return res8
        else:
            question4(answer3)


def check_game(ans4):
    if ans4 == '1':
        print('Have fun learning!\n')
    else:
        main()


def main():
    adventure_name = ask_name()
    script = 'I see you want to become a developer.'
    script2 = "I'll ask you a series of questions to help determine, what lauguage you should learn first"
    print(adventure_name + ", " + script)
    fillers()

    begin_response = begin_game(adventure_name)

    while begin_response != "YES":
        begin_response = ask_begin_again(adventure_name)

    answer1 = question1()

    answer2 = question2(answer1)
    answer3 = question3(answer2)
    answer4 = question4(answer3)
    check_game(answer4)


main()
