from random import random

import random
turns = ['rock', 'paper', 'scissors']
human_turns = []
computer_turns = []


def program():
    print('ROCK PAPER SCISSORS')
    
    human_turn = input('Input your turn:')
    computer_turn = random.choice(turns)
    print('Computer:', computer_turn)

    human_turns .append (human_turn)
    computer_turns .append (computer_turn)

    if human_turn == computer_turn:
        print('Draw!')
    elif human_turn == 'rock' and computer_turn == 'scissors':
        print('You win!')
    elif human_turn == 'paper' and computer_turn == 'rock':
        print('You wins')
    elif human_turn == 'scissors' and computer_turn == 'paper':
        print('You win!')
    else:
        print('You lose')
flag = True
while flag:
    program()
    flag = input('Would you like to play again? [y/n]') == 'y'


print ('You played', len(human_turns), 'times')
print (human_turns)
print (computer_turns)
print ('The game will now end.')
