from board import Board
from players import RandomPlayer, HumanPlayer


class Game:

    def __init__(self):
        self.board = None
        self.players = [None, None]

    def new_game(self):
        self.board = Board()
        self.players = [HumanPlayer("X"), RandomPlayer("O")]
        i = 0  # make it random
        while True:
            self.board.draw()
            print("Player %d turn" % (i + 1))
            move = self.players[i].move(self.board.valid_moves)


if __name__ == "__main__":
    game = Game()
    game.new_game()
