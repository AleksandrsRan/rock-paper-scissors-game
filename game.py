from importlib.resources import contents
from random import random

import random
turns = ['rock', 'paper', 'scissors']
human_turns = []
computer_turns = []
win_history = []


def program():
    print('ROCK PAPER SCISSORS')
    
    human_turn = input('Input your turn:')
    computer_turn = random.choice(turns)
    print('Computer:', computer_turn)

    human_turns .append (human_turn)
    computer_turns .append (computer_turn)


    if human_turn == computer_turn:
        print('Draw!')
        win_history .append ('Draw!')
    elif human_turn == 'rock' and computer_turn == 'scissors':
        print('You win!')
        win_history .append ('You win!')
    elif human_turn == 'paper' and computer_turn == 'rock':
        print('You win!')
        win_history .append ('You win!')
    elif human_turn == 'scissors' and computer_turn == 'paper':
        print('You win!')
        win_history .append ('You win!')
    else:
        print('You lose!')
        win_history .append ('You lose!')
    
flag = True
while flag:
    program()
    flag = input('Would you like to play again? [y/n]') == 'y'


print ('You played', len(human_turns), 'times')
print ('You won', win_history == 'You win!', 'times')
print (human_turns)
print (computer_turns)
print ('The game will now end.')
