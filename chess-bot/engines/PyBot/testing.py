from evaluation import get_evaluation
from bot import get_move

import random
import chess

# Create a random board
def random_board(max_depth=200):
  board = chess.Board()
  depth = random.randrange(0, max_depth)

  for _ in range(depth):
    all_moves = list(board.legal_moves)
    random_move = random.choice(all_moves)
    board.push(random_move)
    if board.is_game_over():
      break

  return board


board = chess.Board("1r6/p1p2ppp/5n2/3k1p2/1b6/5N2/P1PP1PPP/1RB1K2R w K - 0 16")


evaluation = get_move(board, 4)
print("FEN: ", board.fen())
print(board)
print(evaluation)