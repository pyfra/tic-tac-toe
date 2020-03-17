class Board:

    def __init__(self):
        self._board = {x: [" "] * 3 for x in ('A', 'B', 'C')}
        self._rows = ['A', 'B', 'C']
        self._cols = [1, 2, 3]
        self.valid_moves = [self._rows[i] + str(j) for i in range(len(self._rows)) for j in self._cols]

    def draw(self):
        print('-' * 30)
        print('    ' + '   '.join(list(map(str, self._cols))))
        for el, line in self._board.items():
            print(el + ' | ' + ' | '.join(line) + ' |')
        print('-' * 30)

    def _validate_move(self, move):
        try:
            ind = self.valid_moves.index(move)
            return ind
        except ValueError:
            print("Invalid move, please enter one of the valid moves: ")
            print(", ".join(self.valid_moves))
            return -1

    def update_board(self, move, player):
        ind = self._validate_move(move)

        if ind == -1:
            return False
        else:
            _ = self.valid_moves.pop(ind)
            row, col = move
            self._board[row][int(col) - 1] = player.symbol
            return True

    def is_game_over(self, player):
        if len(self.valid_moves) > 5:
            return False, None
        # check rows
        elif self._board['A'][0] == self._board['A'][1] == self._board['A'][2] == player.symbol:
            return True, "win"
        elif self._board['B'][0] == self._board['B'][1] == self._board['B'][2] == player.symbol:
            return True, "win"
        elif self._board['C'][0] == self._board['C'][1] == self._board['C'][2] == player.symbol:
            return True, "win"
        # check cols
        elif self._board['A'][0] == self._board['B'][0] == self._board['C'][0] == player.symbol:
            return True, "win"
        elif self._board['A'][1] == self._board['B'][1] == self._board['C'][1] == player.symbol:
            return True, "win"
        elif self._board['A'][2] == self._board['B'][2] == self._board['C'][2] == player.symbol:
            return True, "win"
        # check diagonals
        elif self._board['A'][0] == self._board['B'][1] == self._board['C'][2] == player.symbol:
            return True, "win"
        elif self._board['A'][2] == self._board['B'][1] == self._board['C'][0] == player.symbol:
            return True, "win"
        elif not len(self.valid_moves):
            return True, "draw"
        else:
            return False, None


class BoardGUI(Board):
    
    def draw(self):
        print('-' * 30)
        print('    ' + '   '.join(list(map(str, self._cols))))
        for el, line in self._board.items():
            print(el + ' | ' + ' | '.join(line) + ' |')
        print('-' * 30)
