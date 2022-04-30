# Create your own adventure with python here
def play():
    x = input("Would you like to play outside or inside?\n")

    if x == "outside":
        x = input('Would you like to go to the park? (Yes or No)\n')
        if x == 'Yes':
            x = input('Which park? Purple or Green\n')
            if x == 'Purple':
                x = input(
                    'We had fun on the swings! Would you like to go home? Yes or No\n')
                if x == 'No':
                    play()
            else:
                x = input(
                    'We had fun on the slide! Would you like to go home? Yes or No\n')
                if x == 'No':
                    play()
        else:
            x = input('Do you want to ride your bike or push your stroller?')
            if x == "bike":
                x = input(
                    'That was a fun ride! Would you like to go home? Yes or No\n')
                if x == 'No':
                    play()
            else:
                x = input(
                    'Baby doll had a great ride! Would you like to go home? Yes or No\n')
                if x == 'No':
                    play()
    else:
        x = input("Would you like to play upstairs or downstairs?\n")
        if x == "upstairs":
            x = input("Would you like to play with your kitchen or read?\n")
            if x == 'read':
                x = input(
                    'I love reading with you! Would you like to play somemore? Yes or No\n')
                if x == 'Yes':
                    play()
            else:
                x = input(
                    'I love playing kitchen! Would you like to play somemore? Yes or No\n')
                if x == 'Yes':
                    play()
        else:
            x = input('Would you like to play on the bed or gym?\n')
            if x == "bed":
                x = input(
                    'No more monkeys jumping on the bed! Would you like to play somemore? Yes or No\n')
                if x == 'Yes':
                    play()
            else:
                x = input(
                    'You are great at yoga! Would you like to play somemore? Yes or No\n')
                if x == 'Yes':
                    play()


play()
