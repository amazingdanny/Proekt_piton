from piece import Piece
from random import random

class Board():
    def __init__(self, size, prob):
        self.__size = size
        self.__prob = prob
        self.__lost = False
        self.__numClicked = 0
        self.__numNonBombs = 0
        self.__board = []
        self.setBoard()

    def replay(self):
        self.__numClicked = 0
        self.__numNonBombs = 0
        self.__board = []
        self.__lost = False


    def setBoard(self):
        for i in range(self.__size[0]):
            row = []
            for col in range(self.__size[1]):
                hasBomb = random() < self.__prob
                if not hasBomb:
                    self.__numNonBombs += 1
                piece = Piece(hasBomb)
                row.append(piece)
            self.__board.append(row)
        self.setNeighbors()

    def setNeighbors(self):
        for row in range(self.__size[0]):
            for col in range(self.__size[1]):
                piece = self.getPiece((row, col))
                neighbors = self.getListOfNeighbors((row, col))
                piece.setNeighborss(neighbors)

    def getListOfNeighbors(self, index):
        neighbors = []
        for row in range(index[0] - 1, index[0] + 2):
            for col in range(index[1] - 1, index[1] + 2):
                outOfBounds = 0
                same = 0
                if row < 0 or row >= self.__size[0] or col < 0 or col >= self.__size[1]:
                    outOfBounds = 1
                if  row == index[0] and col == index[1]:
                    same = 1
                if (same != 1 and outOfBounds != 1):
                    neighbors.append(self.getPiece((row, col)))
        return neighbors


    @property
    def size(self):
        return self.__size

    def getPiece(self, index):
        return self.__board[index[0]][index[1]]

    def handleClick(self, piece, flag):
        if self.getLost():
            return
        if (piece.clicked or (not flag and piece.flagged)):
            return
        if(flag):
            piece.toggleFlag()
            return
        piece.click()
        if piece.bomb:
            self.__lost = True
            return
        self.__numClicked += 1
        if piece.bombsAround != 0:
            return
        for neighbor in piece.getNeighbors():
            if not neighbor.bomb and not neighbor.clicked:
                self.handleClick(neighbor, False)

    def getLost(self):
        return self.__lost
    
    def getWon(self):
        if self.__numNonBombs == self.__numClicked:
            return True
        else: 
            return False