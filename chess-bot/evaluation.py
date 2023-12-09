import positions
import chess

def get_evaluation(board):
    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    print(wp)