from .evaluation import get_evaluation
import numpy as np
from .zobrist import zobrist_hash
from .table import TranspositionTable, TranspositionTableEntry

EXACT=0
transposition_table = TranspositionTable()


# used for the minimax algorithm
def minimax_eval(board):
  return get_evaluation(board)


def minimax(board, depth, alpha, beta, maximizing_player):
  if depth == 0 or board.is_game_over():
    return minimax_eval(board)

  zobrist_key = zobrist_hash(board)
  tt_entry = transposition_table.lookup(zobrist_key)

  if tt_entry and tt_entry.depth >= depth:
      if tt_entry.flag == EXACT:
          return tt_entry.score
      elif tt_entry.flag == LOWER and tt_entry.score >= beta:
          return beta
      elif tt_entry.flag == UPPER and tt_entry.score <= alpha:
          return alpha

  
  if maximizing_player:
    max_eval = -np.inf
    for move in board.legal_moves:
      board.push(move)
      eval = minimax(board, depth - 1, alpha, beta, False)
      board.pop()
      max_eval = max(max_eval, eval)
      alpha = max(alpha, eval)
      if beta <= alpha:
        tt_entry = TranspositionTableEntry(zobrist_key, depth, max_eval, EXACT, move)
        transposition_table.store(tt_entry)

        break
    return max_eval
  else:
    min_eval = np.inf
    for move in board.legal_moves:
      board.push(move)
      eval = minimax(board, depth - 1, alpha, beta, True)
      board.pop()
      min_eval = min(min_eval, eval)
      beta = min(beta, eval)
      if beta <= alpha:
        tt_entry = TranspositionTableEntry(zobrist_key, depth, min_eval, EXACT, move)
        transposition_table.store(tt_entry)

        break
    return min_eval