import numpy as np


class Player:
    def __init__(self, symbol):
        self.symbol = symbol


class RandomPlayer(Player):

    def move(self, valid_moves):
        ind = np.random.uniform(0, len(valid_moves) - 1)
        move = valid_moves[int(ind)]
        print(move)
        return move


class HumanPlayer(Player):

    def move(self, valid_moves):
        return input("please enter the move: ")


class MiniMaxPlayer(Player):
    pass


class MixedPlayer(Player):
    """
    A class that will use the random player with probability 1-p and another (better) player with probability p.
    It will be used to smooth the better player and have intermediate levels of difficulties between the two players
    """

    def __init__(self, p, other_player):
        self.p = p
        self.players = [RandomPlayer(), other_player]

    def move(self, valid_moves):
        i = np.random.binomial(1, self.p)
        return self.players[i]
