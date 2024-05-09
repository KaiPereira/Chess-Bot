import random
import chess
from engines.PyBot.bot import get_move

board = chess.Board("1r6/p1p2ppp/5n2/3k1p2/1b6/5N2/P1PP1PPP/1RB1K2R w K - 0 16")

get_move(board, 4)