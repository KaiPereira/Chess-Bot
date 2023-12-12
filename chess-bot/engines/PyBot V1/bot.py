import chess
import random
import numpy as np
from pathlib import Path
import sys
path_root = "C:\\Users\\keira\\Documents\\VSCode Projects\\Currently Working On\\Chess-Bot\\chess-bot\\engines\\PyBot"
sys.path.append(str(path_root))

from opening import play_opening
from minimax import minimax
from evaluation import get_evaluation


def get_move(board, depth):
    opening_move = play_opening(board)

    if opening_move:
        return opening_move

    top_move = None;

    # Opposite of our minimax
    if board.turn == chess.WHITE:
      top_eval = -np.inf
    else:
      top_eval = np.inf

    for move in board.legal_moves:
        board.push(move)

        # WHEN WE ARE BLACK, WE WANT TRUE AND TO GRAB THE SMALLEST VALUE
        eval = minimax(board, depth - 1, -np.inf, np.inf, board.turn)

        print(eval, move)

        board.pop()

        if board.turn == chess.WHITE:
          if eval > top_eval:
            top_move = move
            top_eval = eval
        else:
          if eval < top_eval:
            top_move = move
            top_eval = eval

    print("CHOSEN MOVE: ", top_move, "WITH EVAL: ", top_eval)
    return top_move