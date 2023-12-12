import chess
from bot import get_move
import chess.svg
import sys


def start_game():
    board = chess.Board()

    while not board.is_game_over():
        move = get_move(board, 4)
        
        print(board, move)

        boardsvg = chess.svg.board(board=board)
        f = open("BoardVisualisedFromFEN.SVG", "w")
        f.write(boardsvg)
        f.close()

        try:
            move = chess.Move.from_uci(move)

            board.push(move)
        except:
            board.push(move)

start_game()