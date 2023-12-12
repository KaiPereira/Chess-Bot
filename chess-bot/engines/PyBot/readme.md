# TO DO

1. Stop the bot from moving before castling
2. Stop the bot from three move stalemating


1. Checkmating
2. Engame
3. Get black working
4. Improvements

# Pawn
Pawn Structure
~~Pawn Center~~
Blockade of Stop
penalty for "d" and "e" pawns blocked on their initial squares

# Knight
~~Decreasing value as pawns disappear~~
Outposts
Knight trapped on A8/H8/A7/H7 or A1/H1/A2/H2 - see Trapped Pieces
Penalty for blocking a C-pawn in closed openings (Crafty defines it as follows: white knight on c3, white pawns on c2 and d4, no white pawn on e4)
When calculating knight mobility, it is advisable to omit squares controlled by enemy pawns
Marginal bonus for a knight defended by a pawn
Penalty for an undefended minor piece (Stockfish)

# Bishop
Bad Bishop
Bishop Pair
Bishop versus Knight
Color Weakness
Fianchetto
Returning Bishop
Bishop trapped by enemy pawns on A2/H2/A7/H7 or on A3/H3/A6/H6, see Trapped Pieces
Penalty for an undefended minor piece (Stockfish)

# Rook
~~Increasing value as pawns disappear~~
Rook on Open File
~~Rook on Seventh (possibly also eigth) rank~~
Tarrasch Rule
Penalty for a Rook blocked by an uncastled King
Small bonus for a rook with enemy queen on the same file (doesn't matter if it's open or not)
Rooks defending each other (Rebel uses a piece/square table for that, making supporeted rook on 7th rank even more valuable)

# Queen
Penalty for early development [1]
Some programs do not evaluate queen mobility
Some versions of Fruit replace queen mobility by king tropism
If king safety evaluation relies on king tropism, queen tends to get somewhat higher bonus

# King
King safety in the middlegame
~~King centralization in the endgame~~
Mate at a Glance
Penalty for standing on a wing with no pawns present in the endgame
Pins/X-ray
Castling Rights