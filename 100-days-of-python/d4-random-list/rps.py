import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps_images = [rock, paper, scissors]

while True:
    player_score = 0
    computer_score = 0

    player = int(input('What do you choose (0 - ROCK, 1 - PAPER, 2 - SCISSOR)? \n'))
    print(rps_images[player])

    print('Computer chose: ')
    computer = random.randint(0,2)
    print(rps_images[computer])

    if player == 0 and computer == 2:
        player_score += 1
    elif player == 2 and computer == 1:
        player_score += 1
    elif player == 1 and computer == 0:
        player_score += 1

    if computer == 0 and player == 2:
        computer_score += 1
    elif computer == 2 and player == 1:
        computer_score += 1
    elif computer == 1 and player == 0:
        computer_score += 1

    if player_score > computer_score:
        print('CONGRATS! You win')
    elif player_score == computer_score:
        print('We have a tie!')
    else:
        print('AWW SHIT! You lose')

    retry = input('Do you want to play again (Y/N)?: ').lower()

    if retry != 'y':
        print('Thank you for playing')
        break

