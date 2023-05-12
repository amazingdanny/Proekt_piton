from piece import Piece
from random import random

class Board():
    def __init__(self, size, prob):
        self.__size = size
        self.__prob = prob
        self.setBoard()

    def setBoard(self):
        self.__board = []
        for row in range(self.__size[0]):
            row = []
            for col in range(self.__size[1]):
                hasBomb = random() < self.__prob
                piece = Piece(hasBomb)
                row.append(piece)
            self.__board.append(row)
        self.setNeighbors()

    def setNeighbors(self):
        for row in range(self.__size[0]):
            for col in range(self.__size[1]):
                piece = self.getPiece((row, col))
                neighbors = self.getListOfNeighbors((row, col))
                piece.setNeighbors(neighbors)

    def getListOfNeighbors(self, index):
        neighbors = []
        for row in range(index[0] - 1, index[0] + 2):
            for col in range(index[0] - 1, index[0] + 2):
                outOfBounds = row < 0 or row >= self.__size[0] or col < 0 or col >= self.__size[1]
                same = row == index[0] and col == index[1]
                if (same or outOfBounds):
                    continue
                neighbors.append(self.getPiece((row, col)))
        return neighbors


    @property
    def size(self):
        return self.__size

    def getPiece(self, index):
        return self.__board[index[0]][index[1]]
