class Board():
    def __init__(self, size):
        self.__size = size
        self.setBoard()

    def setBoard(self):
        self.__board = []
        for row in range(self.__size[0]):
            row = []
            for col in range(self.__size[1]):
                piece = None
                row.append(piece)
            self.__board.append(row)

    @property
    def size(self):
        return self.__size

        