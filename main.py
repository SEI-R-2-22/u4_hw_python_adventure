def fight_arena():
    print('Welcome to Fight Arena! Choose your NFT character...')

    character = input(' Women and Weapons, Creature, Notorious Ninja : ')

    if character == 'Women and Weapons':
        print('Choose your oponent')
        oponent = input('Creature, Notorious Ninja :')
        if oponent == 'Creature':
            print('Round 1')
            print('Fight!')
            print('Creature is tough, but he carries no weapon! Choose your weapon.')
            weapon = input('bare knuckles, sword, nunchucks :')
            if weapon == 'bare knuckles':
                print('oh no creature is hugging you, you lost to hugs.')
                play_again = input('play again? yes  no :')
                if play_again == 'yes':
                    return fight_arena()
                else: 
                    print('You lose')
            if weapon == 'nunchucks':
                print('tough battle')  
                print('Creature is dogging the nunchucks!')
                print('It is a draw')
                play_again = input('play again? yes  no :')
                if play_again == 'yes':
                    return fight_arena()
                else:
                    print('Til next time')        
            if weapon == 'sword':
                print('SLICED Creature! ')
                print('Round 2, Ninja replaces Creature!')
                print('Ninja has a knife!')
                change_weapon = input('keep weapon or change ?')
                if change_weapon == 'keep weapon':
                        print('Women and Weapon wins!')
                if change_weapon == 'change':
                    weapon = input('bare knuckles, nunchucks :') 
                    if weapon == 'bare knuckles':  
                        print('You have been chopped!')
                    if weapon == 'nunchucks':
                        print('tough battle')  
                        print('It is a draw')
                    play_again = input('play again? yes  no :')
                    if play_again == 'yes':
                        return fight_arena()
                    else: 
                        print('Til next time')
        if oponent == 'Notorious Ninja':
            print('Round 1')
            print('Fight!')
            print('Ninja is notorious! Choose your weapon.')
            weapon = input('bare knuckles, sword, nunchucks :')
            if weapon == 'bare knuckles':
                print('Ninja chopped WAW')
                play_again = input('play again? yes  no :')
                if play_again == 'yes':
                    return fight_arena()
                else: 
                    print('You lose')
            if weapon == 'nunchucks':
                print('tough battle')  
                print('Ninja is using nunchucks too!')
                print('It is a draw')
                play_again = input('play again? yes  no :')
                if play_again == 'yes':
                    return fight_arena()
                else:
                    print('Til next time')        
            if weapon == 'sword':
                print('SLICED Ninja! ')
                print('Round 2, Creature is fighting!')
                print('Creature is giving hugs')
                change_weapon = input('keep weapon or change ?')
                if change_weapon == 'keep weapon':
                        print('Women and Weapon wins!')
                if change_weapon == 'change':
                    weapon = input('bare knuckles, nunchucks :') 
                    if weapon == 'bare knuckles':  
                        print('WAW loses to Creature hugs :( ')
                    if weapon == 'nunchucks':
                        print('tough battle, Creature is slipping')  
                        print('It is a draw')
                play_again = input('play again? yes  no :')
                if play_again == 'yes':
                    return fight_arena()
                else: 
                    print('Til next time')    
    if character == 'Creature':
        print('Choose your oponent')
        oponent = input('Women and Weapons, Notorious Ninja:')
        if oponent == 'Women and Weapons':
            print('Round 1')
            print('Fight!')
            print('WAW is tough! Choose your weapon.')
            weapon = input('hugs, slips, love :')
            if weapon == 'hugs':
                print('You win with hugs :) ')
                play_again = input('play again? yes  no :')
                if play_again == 'yes':
                    return fight_arena()
                else: 
                    print('Xoxo')
            if weapon == 'slips':
                print('tough battle')  
                print('It is a draw')
                play_again = input('play again? yes  no :')
                if play_again == 'yes':
                    return fight_arena()
                else:
                    print('Til next time')        
            if weapon == 'love':
                print('Love beats all! ')
                print('Round 2, Ninja replaces WAW!')
                print('Ninja has a knife!')
                change_weapon = input('keep weapon or change ?')
                if change_weapon == 'keep weapon':
                        print('Creature wins!')
                if change_weapon == 'change':
                    weapon = input('hugs, slips :') 
                    if weapon == 'hugs':  
                        print('You have been chopped!')
                    if weapon == 'slips':
                        print('tough battle')  
                        print('It is a draw')
                play_again = input('play again? yes  no :')
                if play_again == 'yes':
                    return fight_arena()
                else: 
                    print('Til next time')
        if oponent == 'Notorious Ninja':
            print('Round 1')
            print('Fight!')
            print('Ninja is notorious! Choose your weapon.')
            weapon = input('hugs, slips, love :')
            if weapon == 'hugs':
                print('Creature got chopped to pieces ')
                play_again = input('play again? yes  no :')
                if play_again == 'yes':
                    return fight_arena()
                else: 
                    print('til next time')
            if weapon == 'slips':
                print('tough battle')  
                print('It is a draw')
                play_again = input('play again? yes  no :')
                if play_again == 'yes':
                    return fight_arena()
                else:
                    print('Til next time')        
            if weapon == 'love':
                print('Love beats all! ')
                print('Round 2, WAW replaces Ninja!')
                print('WAW has a sword!')
                change_weapon = input('keep weapon or change ?')
                if change_weapon == 'keep weapon':
                        print('Creature wins!')
                if change_weapon == 'change':
                    weapon = input('hugs, slips :') 
                    if weapon == 'hugs':  
                        print('You have been chopped!')
                    if weapon == 'slips':
                        print('tough battle')  
                        print('It is a draw')
                    play_again = input('play again? yes  no :')
                    if play_again == 'yes':
                        return fight_arena()
                    else: 
                        print('Til next time')    
    if character == 'Notorious Ninja':
        print('Choose your oponent')
        oponent = input('Women and Weapons, Creature:')
        if oponent == 'Creature':
            print('Round 1')
            print('Fight!')
            print('Creature is tough, but he carries no weapon! Choose your weapon.')
            weapon = input('kicks, sword, nunchucks :')
            if weapon == 'kicks':
                print('oh no creature is hugging you, you lost to hugs.')
                play_again = input('play again? yes  no :')
                if play_again == 'yes':
                    return fight_arena()
                else: 
                    print('You lose')
            if weapon == 'nunchucks':
                print('tough battle')  
                print('Creature is dogging the nunchucks!')
                print('It is a draw')
                play_again = input('play again? yes  no :')
                if play_again == 'yes':
                    return fight_arena()
                else:
                    print('Til next time')        
            if weapon == 'sword':
                print('SLICED Creature! ')
                print('Round 2, WAW replaces Creature!')
                print('WAW has a gun')
                change_weapon = input('keep weapon or change ?')
                if change_weapon == 'keep weapon':
                        print('Women and Weapon wins!')
                if change_weapon == 'change':
                    weapon = input('kicks, nunchucks :') 
                    if weapon == 'kicks':  
                        print('You have been shot!')
                    if weapon == 'nunchucks':
                        print('tough battle, you redirected the bullets')  
                        print('It is a draw')
                play_again = input('play again? yes  no :')
                if play_again == 'yes':
                    return fight_arena()
                else: 
                    print('Til next time')
        if oponent == 'WAW':
            print('Round 1')
            print('Fight!')
            print('WAW is fierce! Choose your weapon.')
            weapon = input('kicks, sword, nunchucks :')
            if weapon == 'sword':
                print('Ninja chopped WAW')
                play_again = input('play again? yes  no :')
                if play_again == 'yes':
                    return fight_arena()
                else: 
                    print('You lose')
            if weapon == 'nunchucks':
                print('tough battle')  
                print('WAW is using nunchucks too!')
                print('It is a draw')
                play_again = input('play again? yes  no :')
                if play_again == 'yes':
                    return fight_arena()
                else:
                    print('Til next time')        
            if weapon == 'kicks':
                print('Ninja kicks are notorious! ')
                print('Round 2, Creature is fighting!')
                print('Creature is giving hugs')
                change_weapon = input('keep weapon or change ?')
                if change_weapon == 'keep weapon':
                        print(' Creature hugs are notorious! Creature wins!')
                if change_weapon == 'change':
                    weapon = input('sword, nunchucks :') 
                    if weapon == 'sword':  
                        print('Notorious Ninja slices Creature ')
                    if weapon == 'nunchucks':
                        print('tough battle, Creature is slipping')  
                        print('It is a draw')
                play_again = input('play again? yes  no :')
                if play_again == 'yes':
                    return fight_arena()
                else: 
                    print('Til next time') 
        
fight_arena()