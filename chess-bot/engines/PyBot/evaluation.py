from .material import get_material
import chess
from . import positions


def piece_position_evaluation(board, type, pieces_left):

    piece_positions = None;
    piece_evaluations = 0;


    amount_pieces_for_engame = 17

    match type:
        case chess.PAWN:
            if pieces_left < amount_pieces_for_engame:
                piece_positions = positions.pawn_end
            else:
                piece_positions = positions.pawn
        case chess.KNIGHT:
            piece_positions = positions.knight
        case chess.BISHOP:
            piece_positions = positions.bishop
        case chess.ROOK:
            piece_positions = positions.rook
        case chess.QUEEN:
            piece_positions = positions.queen
        case chess.KING:
            if pieces_left < amount_pieces_for_engame:
                piece_positions = positions.king_end
            else:
                piece_positions = positions.king
        

    for piece in board.pieces(type, chess.WHITE):
        piece_evaluations += piece_positions[piece]

    for piece in board.pieces(type, chess.BLACK):
        piece_evaluations -= piece_positions[::-1][piece]

    return piece_evaluations



def get_evaluation(board):

    # Check for checkmate of the opponent
    if board.is_checkmate():
        if board.turn:
            return -9999
        else:
            return 9999
    if board.is_stalemate():
            return 0
    if board.is_insufficient_material():
            return 0


    total_material, pieces_left = get_material(board)
    

    # How many pieces until it's engame
    endgame_amount_pieces = 17


    # Pawns try to promote in engame
    pawn_positions = None;

    if pieces_left < endgame_amount_pieces:
        pawn_positions = positions.pawn_end
    else:
        pawn_positions = positions.pawn


    pawnsq = sum([pawn_positions[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
    pawnsq = pawnsq + sum([-pawn_positions[chess.square_mirror(i)]
                        for i in board.pieces(chess.PAWN, chess.BLACK)])
    knightsq = sum([positions.knight[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)])
    knightsq = knightsq + sum([-positions.knight[chess.square_mirror(i)]
                            for i in board.pieces(chess.KNIGHT, chess.BLACK)])
    bishopsq = sum([positions.bishop[i] for i in board.pieces(chess.BISHOP, chess.WHITE)])
    bishopsq = bishopsq + sum([-positions.bishop[chess.square_mirror(i)]
                            for i in board.pieces(chess.BISHOP, chess.BLACK)])
    rooksq = sum([positions.rook[i] for i in board.pieces(chess.ROOK, chess.WHITE)])
    rooksq = rooksq + sum([-positions.rook[chess.square_mirror(i)]
                        for i in board.pieces(chess.ROOK, chess.BLACK)])
    queensq = sum([positions.queen[i] for i in board.pieces(chess.QUEEN, chess.WHITE)])
    queensq = queensq + sum([-positions.queen[chess.square_mirror(i)]
                            for i in board.pieces(chess.QUEEN, chess.BLACK)])


    # Kings tries to go to the middle in engame
    kings_positions = None;

    if pieces_left < endgame_amount_pieces:
        kings_positions = positions.king_end
    else:
        kings_positions = positions.king
    
    kingsq = sum([kings_positions[i] for i in board.pieces(chess.KING, chess.WHITE)])
    kingsq = kingsq + sum([-kings_positions[chess.square_mirror(i)]
                        for i in board.pieces(chess.KING, chess.BLACK)])

    eval = total_material + pawnsq + knightsq + rooksq + queensq + kingsq 

    return eval