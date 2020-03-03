import numpy as np


class Player:
    def __init__(self, symbol):
        self.symbol = symbol


class RandomPlayer(Player):

    def move(self, valid_moves):
        ind = np.random.uniform(0, len(valid_moves - 1))
        return valid_moves[int(ind)]


class HumanPlayer(Player):

    def move(self, valid_moves):
        return input("please enter the move: ")