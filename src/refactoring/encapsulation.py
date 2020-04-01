#!/usr/bin/env python3
"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space exactly 100 wins.
Object-oriented with a Player and Game objects
"""


import random


class Player:
    _target_score = 100  # hidden and 'private'

    def __init__(self, player_num):
        self.score = 0
        self.player_num = player_num

    def make_move(self):
        dice = random.randint(1, 6)
        if self.score + dice > 100:
            pass
        else:
            self.score += dice
            print(f'{self} roll a {dice} (score: {self.score})')

    def met_goal(self):
        return self.score == self._target_score

    def __str__(self):
        return f'Player {self.player_num}'


class Game:
    def __init__(self, num_players):
        self.players = []
        try:
            if num_players > 1:
                for i in range(1, num_players):
                    self.players.append(Player(i))
            else:
                raise ValueError(
                    'Number of players must be an integer and greater than 1')
        except ValueError as e:
            print(f'Error: {e}')

    def start_game(self):
        print('Start Game!')
        while True:
            for player in self.players:
                player.make_move()
                if player.met_goal():
                    print(f'{player} won!')
                    print()
                    return

    def final_score(self):
        for player in self.players:
            print(f'{player} score: {player.score}')


game = Game(num_players=4)
game.start_game()
game.final_score()

for i in range(2, 5):
    game = Game(num_players=i)
    game.start_game()
    game.final_score()
