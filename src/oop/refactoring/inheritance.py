#!/usr/bin python3
"""
Simulate a simple board game
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space exactly 100n wins.
Object-oriented with a LuckPlayer and Game Objects.
"""

import random


class Player:
    def __init__(self, player_num):
        self.score = 0
        self.player_num = player_num

    def roll_dice(self):
        return random.randint(1, 6)

    def make_move(self):
        roll = self.roll_dice()
        if self.score + roll > 100:
            pass
        else:
            self.score += roll
            print(f'{self} roll a {roll} (score: {self.score})')

    def met_goal(self):
        return self.score == 100

    def __str__(self):
        return f'Player {self.player_num}'


class LuckyPlayer(Player):
    def roll_dice(self):
        number = random.randint(3, 6)
        print(f'{self} roll a {number}')
        return number

    def __str__(self):
        string = super().__str__()
        return string + ' (lucky)'


class Game(object):
    def __init__(self, num_players):
        self.players = []
        player_types = [Player, LuckyPlayer]
        for i in range(1, num_players + 1):
            player_type = random.choice(player_types)
            self.players.append(player_type(i))

    def start_game(self):
        print('START GAME!')
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
