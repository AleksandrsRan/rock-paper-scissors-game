def program():
    print('ROCK PAPER SCISSORS')
    human_turn = input('Input your turn:')

    import random
    turns = ['rock', 'paper', 'scissors']
    computer_turn = random.choice(turns)
    print('Computer:', computer_turn)


    if human_turn == computer_turn:
        print('Draw!')
    elif human_turn == 'rock' and computer_turn == 'scissors':
        print('You win!')
    elif human_turn == 'paper' and computer_turn == 'rock':
        print('You wins')
    elif human_turn == 'scissors' and computer_turn == 'paper':
        print('You win!')
    elif human_turn == 'scissors' and computer_turn == 'rock':
        print('You lose!')
    elif human_turn == 'rock' and computer_turn == 'paper':
        print('You lose')
    elif human_turn == 'paper' and computer_turn == 'scissors':
        print('You lose!')
    else:
        print('Next time input rock, paper or scissors')
flag = True
while flag:
    program()
    flag = input('Would you like to run the program again? [y/n]') == 'y'

print ("The program will now stop.")
