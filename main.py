from minesweeper import Minesweeper
from board import Board
size = (12, 12)
board = Board(size, 0.2)
scsize = (800, 800)
game = Minesweeper(board, scsize)
game.run() 