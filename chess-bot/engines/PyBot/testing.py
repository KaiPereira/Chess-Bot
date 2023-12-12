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


board = chess.Board("r1bqkb1r/ppppn2p/5p2/1B2p3/1n6/2N2N2/PPPP1PPP/R1BQK2R w KQkq - 2 7")


evaluation = get_move(board, 4)
print("FEN: ", board.fen())
print(board)
print(evaluation)