from material import get_material
import chess
import positions


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
    if (board.turn == chess.WHITE) & board.is_checkmate():
        return -99999
    elif (board.turn == chess.BLACK) & board.is_checkmate():
        return 99999

    material, pieces_left = get_material(board)

    pawn_p_eval = piece_position_evaluation(board, chess.PAWN, pieces_left)
    knight_p_eval = piece_position_evaluation(board, chess.KNIGHT, pieces_left)
    bishop_p_eval = piece_position_evaluation(board, chess.BISHOP, pieces_left)
    rook_p_eval = piece_position_evaluation(board, chess.ROOK, pieces_left)
    king_p_eval = piece_position_evaluation(board, chess.KING, pieces_left)
    queen_p_eval = piece_position_evaluation(board, chess.QUEEN, pieces_left)

    position_eval = pawn_p_eval + knight_p_eval + bishop_p_eval + rook_p_eval + king_p_eval + queen_p_eval

    eval = material + position_eval


    # If it's going to be stalemate and our eval is higher then set it to 0
    if board.is_stalemate():
        return 0

    return eval