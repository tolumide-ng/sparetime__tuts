#!/usr/bin/env python3

"""
Simulate a simple board game.
There are 2 players.
Eachg player takes turn rolling a die and moving that number of spaces.
The first person to get exactly 100 wins.
Using procedural/imperative programming but refacrtored and abstracted
"""


import random

scores = [0, 0]

print('Start Game')

while True:
    for player_num in range(1, 3):
        dice = random.randint(1, 6)

        if scores[player_num - 1] + dice > 100:
            continue

        scores[player_num - 1] += dice
        new_score = scores[player_num - 1]
        print(f'Player {player_num} rolls a {dice} (score: {new_score})')
        if new_score == 100:
            print(f'Player {player_num} wins!')
            break
    else:
        continue
    break

print()
print('Final Score:')
print(f'Player : {scores[0]}')
print(f'Player : {scores[1]}')
