from board import Board
from players import RandomPlayer, HumanPlayer


class Game:

    def __init__(self):
        self.board = None
        self.players = [None, None]

    def _initialize_game(self):
        self.board = Board()
        computer = True if input('Do you want to play against the computer (Y or N): ') == 'Y' else False
        if computer:
            start = True if input('Do you want to play first (Y or N): ') == 'Y' else False
            if start:
                self.players = [HumanPlayer("X"), RandomPlayer("O")]
            else:
                self.players = [RandomPlayer("X"), HumanPlayer("O")]
        else:
            self.players = [HumanPlayer("X"), HumanPlayer("O")]
        self.i = 0
        print('#' * 30)
        print('Game begins')
        print('#' * 30)
        self.board.draw()

    def new_game(self):
        self._initialize_game()
        while True:
            print('-' * 30)
            print("Player %d turn" % (self.i + 1))
            move = self.players[self.i].move(self.board.valid_moves)
            next_player = self.board.update_board(move, self.players[self.i])
            self.board.draw()
            stop, status = self.board.is_game_over(self.players[self.i])
            if stop:
                print('game is over!')
                if status == 'win':
                    print('Player %d wins!' % (self.i+1))
                else:
                    print('It was a draw!')

                key = input('Enter Y to play another game, any other keys to exit: ')
                if key == 'Y':
                    self._initialize_game()
                    next_player = False
                else:
                    break

            if next_player:
                self.i = 0 if self.i == 1 else 1


if __name__ == "__main__":
    game = Game()
    game.new_game()
