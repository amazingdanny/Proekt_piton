from minesweeper import Minesweeper
from board import Board
size = (9, 9)
board = Board(size, 0.1)
scsize = (800, 800)
game = Minesweeper(board, scsize)
game.run() 