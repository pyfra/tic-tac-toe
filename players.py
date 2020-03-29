import numpy as np
import copy
import os
from sklearn.preprocessing import OneHotEncoder


class Player:
    def __init__(self, symbol, *args, **kwargs):
        self.symbol = symbol
        assert self.symbol in ["X",
                               "O"], "unsupported symbol %s, the only possible symbols supported now are X and O" % self.symbol

    def move(self, *args, **kwargs):
        raise NotImplementedError()


class RandomPlayer(Player):

    def move(self, valid_moves, *args, **kwargs):
        ind = np.random.uniform(0, len(valid_moves) - 1)
        move = valid_moves[int(ind)]
        print(move)
        return move


class HumanPlayer(Player):

    def move(self, valid_moves, *args, **kwargs):
        return input("please enter the move: ")


class MiniMaxPlayer(Player):
    _MAPPING_GAME = {
        'win': 1,
        'draw': 0
    }

    def __init__(self, symbol, other_player):
        self.other = other_player
        self.moves_scores = None
        super(MiniMaxPlayer, self).__init__(symbol)

    def move(self, valid_moves, board, *args, **kwargs):
        score, move, mapping_move_scores = self._evaluate_best_move(valid_moves, board, self, 1, 0)
        self.moves_scores = mapping_move_scores
        return move

    def _evaluate_best_move(self, valid_moves, board, player, multiplier, i):
        scores_moves = list()
        mapping_moves_scores = dict()
        min_or_max = [max, min]  # apply min or max according to which player move is being evaluated
        for move in valid_moves:
            # create  copy of the board
            board_copy = copy.deepcopy(board)
            board_copy.update_board(move, player)
            is_over, result = board_copy.is_game_over(player)
            if is_over:
                score = self._MAPPING_GAME[result] * multiplier
            else:
                new_player = self.other if player == self else self
                new_multiplier = 1 if multiplier == -1 else -1
                new_i = 0 if i == 1 else 1
                score, _, _ = self._evaluate_best_move(board_copy.valid_moves, board_copy, new_player, new_multiplier,
                                                       new_i)
            scores_moves.append(score)
            mapping_moves_scores[move] = score
        min_or_max_score = min_or_max[i](scores_moves)
        return min_or_max_score, valid_moves[scores_moves.index(min_or_max_score)], mapping_moves_scores

    def _visualize_scores(self):
        print(self.moves_scores)


class DLPlayer(Player):

    def __init__(self, symbol):
        """
        Look for file where model is saved otherwise train it!
        """
        # check if file exists
        super(DLPlayer, self).__init__(symbol)
        target_file = os.path.join(os.path.dirname(__file__), 'trained_models', 'nn_model.h5')
        if os.path.isfile(target_file):
            from keras.models import load_model
            self.nn = load_model(target_file)
        else:
            raise NotImplementedError('There is no saved models, you might want to train your own DL model and save it')

        other_symbol = "O" if self.symbol == "X" else "X"

        self._labels_encoding = {
            ' ': 0,
            other_symbol: 1,
            self.symbol: 2,  # always need to map out player to X
        }

        self._moves_mapping = []

    def move(self, valid_moves, board, *args, **kwargs):
        encoded_board = self._encode_board_status(board)
        encoded_moves = self._encode_valid_moves(valid_moves)
        all_boards = self._get_all_possible_board_states(encoded_board, encoded_moves)

    def _encode_valid_moves(self, moves):
        return [self._map_move(move) for move in moves]

    def _get_all_possible_board_states(self, encoded_board, encoded_valid_moves):
        expanded_board = np.tile(encoded_board, (len(encoded_valid_moves), 1))
        for i, move in enumerate(encoded_valid_moves):
            expanded_board[i, move] = self._labels_encoding["X"]

        return expanded_board

    def _encode_board_status(self, board):
        target_array = self._flatten_board(board)
        encoded_board = np.vectorize(self._labels_encoding.get)(target_array)
        return encoded_board

    def _flatten_board(self, board):
        target_list = []
        for _, l in board._board.items():
            target_list += l

        return np.array(target_list)
    @staticmethod
    def _map_move(move):
        _map = {'A': 0, 'B': 3, 'C': 6}
        row, col = move
        return _map[row] + int(col) - 1

class MixedPlayer(Player):
    """
    A class that will use the random player with probability 1-p and another (better) player with probability p.
    It will be used to smooth the better player and have intermediate levels of difficulties between the two players
    """

    def __init__(self, other_player, p):
        self.p = p
        self.players = [RandomPlayer(other_player.symbol), other_player]
        self.symbol = other_player.symbol

    def move(self, valid_moves, *args, **kwargs):
        i = np.random.binomial(1, self.p)
        return self.players[i].move(valid_moves, *args, **kwargs)
