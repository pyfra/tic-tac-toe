import numpy as np
import copy


class Player:
    def __init__(self, symbol, *args, **kwargs):
        self.symbol = symbol


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
        min_or_max = [max, min] # apply min or max according to which player move is being evaluated
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
                score, _, _ = self._evaluate_best_move(board_copy.valid_moves, board_copy, new_player, new_multiplier, new_i)
            scores_moves.append(score)
            mapping_moves_scores[move] = score
        min_or_max_score = min_or_max[i](scores_moves)
        return min_or_max_score, valid_moves[scores_moves.index(min_or_max_score)], mapping_moves_scores

    def _visualize_scores(self):
        print(self.moves_scores)


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
