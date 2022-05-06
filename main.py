# Create your own adventure with python here
import random

player = {
    'name': ''
}

baby_needs = ['diaper', 'formula', 'paci', 'rock']

random_index = None

solution = None

partner = ', Your partner calmed the baby down by'


def calm_baby():
    print('Good Job', player['name'] +
          ', you\'ve successfully calmed baby!')
    play_again()


def create_solution():
    global random_index
    global solution
    random_index = random.randint(0, 3)
    solution = baby_needs[random_index]
    greeting()


def invalid():
    print('Please enter a valid answer.')


def play_again():
    print('Want to try again?\n[1]Yes\n[2]No')
    answer = input()
    if answer == '1':
        start_game()
    elif answer == '2':
        print('goodbye')
    else:
        invalid()
        play_again()


def partner_calms_baby():
    if solution == 'diaper':
        print(
            player['name'] + partner, 'by changing their diaper.')
    elif solution == 'formula':
        print(player['name'] + partner, 'giving baby formula.')
    elif solution == 'paci':
        print(player['name'] + partner, 'giving baby a pacifier.')
    elif solution == 'rock':
        print(player['name'] + partner, 'rocking baby back to sleep.')
    play_again()


def pretend_sleep():
    print(player['name'] +
          ', Your partner wakes up and kicks you...what do you do?')
    answer = input(
        '[1]Keep pretending that you\'re sleeping\n[2]Get up to see what\'s going on.\n')
    if answer == '1':
        partner_calms_baby()
    elif answer == '2':
        get_up()
    else:
        invalid()
        pretend_sleep()


def get_up():
    print(player['name'] + ', You stumble your way to the nursery door and notice the crying isn\'t as loud as before. What do you do?')
    answer = input(
        '[1]Turn around and go back to your room to sleep\n[2]Go inside nursery.\n')
    if answer == '1':
        print('Just as you turn around, baby starts crying louder than before waking up your partner...')
        partner_calms_baby()
    elif answer == '2':
        go_inside()
    else:
        invalid()
        get_up()


def diaper_change():
    if solution == 'diaper':
        print('You quickly change baby\'s diaper and baby stops crying!')
        calm_baby()
    else:
        print('You took too long to change baby\'s diaper! It made baby cry even louder and your partner has woken up!')
        partner_calms_baby()


def give_bottle():
    if solution == 'formula':
        print('You give baby a bottle of warm formula and baby falls asleep drinking it.')
        calm_baby()
    else:
        print('You forgot to warm the bottle! The cold formula made baby cry even louder and your partner has woken up!')
        partner_calms_baby()


def give_paci():
    if solution == 'paci':
        print(
            'You turn on baby\'s night light and give baby a pacifier. Baby stops crying.')
        calm_baby()
    else:
        print('You didn\'t turn the lights on when trying to give pacifier to baby. You ended up poking baby in the eye making baby cry even louder. Your partner has woken up!')
        partner_calms_baby()


def rock_baby():
    if solution == 'rock':
        print('You gently rock baby back and forth while shushing...Baby falls alseep immediately!')
        calm_baby()
    else:
        print('Your rocking had no rhythm! Baby did not like it and crys even louder. Your partner has woken up!')
        partner_calms_baby()


def go_inside():
    print(player['name'] +
          ', You\'ve seen your partner do this a million times! What do you do?')
    answer = input(
        '[1]Change baby\'s diaper\n[2]Give baby bottle of formula\n[3]Give baby a pacifier\n[4]Rock baby back to sleep')
    if answer == '1':
        diaper_change()
    elif answer == '2':
        give_bottle()
    elif answer == '3':
        give_paci()
    elif answer == '4':
        rock_baby()
    else:
        invalid()
        go_inside()


def greeting():
    if player['name'] == '':
        player['name'] = input('What is your name?\n')
    print(player['name'] +
          ', It\'s 3am in the morning and you wake up to your baby crying...what do you do?')
    answer = input(
        '[1]Pretend you\'re still sleeping and wait for your partner to wake up\n[2]Get up to see what\'s going on.\n')
    if answer == '1':
        pretend_sleep()
    elif answer == '2':
        get_up()
    else:
        invalid()
        greeting()


def start_game():
    create_solution()


start_game()
