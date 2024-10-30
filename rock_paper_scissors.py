# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 10:34:45 2024

@author: Regan
"""
#importing random and setting up winner variable
import random

winner = ''

#mapping random number selection to corresponding string
random_choice = random.randint(0, 2)
#remember to programmer sequences of #s start at 0

if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'
    
#get users input
user_choice = input('rock, paper or scissors?')

#game logic
if computer_choice == user_choice:
    winner = 'Tie'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'Computer'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'Computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'Computer'
else:
    winner = 'User'
    
#announce winner and choices 
if winner == 'Tie':
    print('We both chose', computer_choice + ', play again.')
else:
    print(winner, 'won. The computer chose', computer_choice + '.')