import chess

def get_material(board):
    # White
    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    wr = len(board.pieces(chess.PAWN, chess.WHITE))
    wk = len(board.pieces(chess.PAWN, chess.WHITE))
    wb = len(board.pieces(chess.PAWN, chess.WHITE))
    wq = len(board.pieces(chess.PAWN, chess.WHITE))

    # Black
    bp = len(board.pieces(chess.PAWN, chess.WHITE))
    br = len(board.pieces(chess.PAWN, chess.WHITE))
    bk = len(board.pieces(chess.PAWN, chess.WHITE))
    bb = len(board.pieces(chess.PAWN, chess.WHITE))
    bq = len(board.pieces(chess.PAWN, chess.WHITE))