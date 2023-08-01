print('''
                           ___
                          ( ((
                           ) ))
  .::.                    / /(
 'M .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._
(J ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>
 `P `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''
  `::'                    \ \(
                           ) ))
                          (_((

      ''')
print("Welcome to my fucking basic shit game.")
print("Your mission is to find the treasure.\n")

direction = input('Do you want to go left or right (left/right)?: ').lower()

if direction == 'left':
    choice_2 = input('Awesome! You have found a lake. Do you want to swim or wait(swim/wait)?: ').lower()
    if choice_2 == 'wait':
        door = input('3 Doors appeared! Which color do you choose(red/yellow/blue)?: ').lower()
        if door == 'red':
            print('This door is a shortcut to HELL. You are BURNED. GAME OVER')
        elif door == 'blue':
            print('There are a pack of beasts and you became their LUNCH. GAME OVER')
        elif door == 'yellow':
            print('NICE CHOICE! You have found a treasure full of SHIT! Congrats on making it ALIVE!')
        else:
            print('Incorrect color! You have been devoured by an unknown SHIT. GAME OVER')
    else:
        print('FVCKER! You encountered a trout and attacked you! YOU ARE DEAD!')
else:
    print('\nOops..you fell into the butthole!. GAME OVER')