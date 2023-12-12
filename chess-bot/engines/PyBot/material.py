import chess

def get_material(board):
    # Weights
    pw = 100
    kw = 310
    bw = 330
    rw = 500
    qw = 900
    kingw = 2000

    # Decreased value of knight per pawn gone
    knight_less_pawns_weight = 10

    # Increase value of rook per enemy pawn gone
    rook_less_pawns_weight = 20

    # If knight vs bishop


    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    wr = len(board.pieces(chess.ROOK, chess.WHITE))
    wk = len(board.pieces(chess.KNIGHT, chess.WHITE))
    wb = len(board.pieces(chess.BISHOP, chess.WHITE))
    wq = len(board.pieces(chess.QUEEN, chess.WHITE))
    wking = len(board.pieces(chess.KING, chess.WHITE))

    bp = len(board.pieces(chess.PAWN, chess.BLACK))
    br = len(board.pieces(chess.ROOK, chess.BLACK))
    bk = len(board.pieces(chess.KNIGHT, chess.BLACK))
    bb = len(board.pieces(chess.BISHOP, chess.BLACK))
    bq = len(board.pieces(chess.QUEEN, chess.BLACK))
    bking = len(board.pieces(chess.KING, chess.BLACK))



    knight_bishop_engame_eval = 0;


    # If it's just a knight vs bishop, knight get a +20 eval
    if (wr == 0) & ((wk == 1) & (bb == 1)) & (wb == 0) & (wq == 0):
        knight_bishop_engame_eval = -20;
    elif (wr == 0) & ((bk == 1) & (wb == 1)) & (bb == 0) & (wq == 0):
        knight_bishop_engame_eval = 20

    # White
    wpw = wp * pw
    # Rook weight increases for less pawns
    wrw = wr * (rw + ((2 - br) * rook_less_pawns_weight))
    # Knight weight goes down for each enemy pawn gone (8 pawns)
    wkw = wk * (kw - ((8 - bp) * knight_less_pawns_weight))
    wbw = wb * bw
    wqw = wq * qw
    wkingw = wking * kingw

    # Black
    bpw = bp * pw
    # Rook weight increases for less pawns
    brw = br * (rw + ((2 - wr) * rook_less_pawns_weight))
    # Knight weight goes down for each enemy pawn gone  (8 pawns)
    bkw = bk * (kw - ((8 - wp) * knight_less_pawns_weight))
    bbw = bb * bw
    bqw = bq * qw
    bkingw = bking * kingw

    white_material = wpw + wrw + wkw + wbw + wqw + wkingw
    black_material = bpw + brw + bkw + bbw + bqw + bkingw

    total_material = white_material - black_material + knight_bishop_engame_eval

    pieces_left = wp + wk + wb + wr + wq + bp + bk + bb + br + bq

    return total_material, pieces_left