class TranspositionTable:
    def __init__(self):
        self.table = {}

    def lookup(self, zobrist_key):
        return self.table.get(zobrist_key)

    def store(self, entry):
        self.table[entry.zobrist_key] = entry


class TranspositionTableEntry:
    def __init__(self, zobrist_key, depth, score, flag, best_move):
        self.zobrist_key = zobrist_key
        self.depth = depth
        self.score = score
        self.flag = flag
        self.best_move = best_move