import chess
import chess.engine


def get_move(board):
    stockfish = chess.engine.SimpleEngine.popen_uci("/workspaces/Chess-Bot/chess-bot/engines/StockfishGambit/stockfish.tar")

    move = engine.play(board,
                chess.engine.Limit(time=1),
                ponder=False)

    print(move)


board = chess.Board()

get_move(board)