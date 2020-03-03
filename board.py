class Board:

    def __init__(self):
        self._board = {x: [" "] * 3 for x in ('A', 'B', 'C')}
        self._rows = ['A', 'B', 'C']
        self._cols = [1, 2, 3]
        self.valid_moves = [self._rows[i] + str(self._cols[i]) for i in range(len(self._rows))]

    def draw(self):
        print('-' * 30)
        print('    ' + '   '.join(list(map(str, self._cols))))
        for el, line in self._board.items():
            print(el + ' | ' + ' | '.join(line) + ' |')
        print('-' * 30)
