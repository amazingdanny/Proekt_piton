class Piece():
    def __init__(self, hasBomb):
        self.__hasBomb = hasBomb
        self.__clicked = False
        self.__flagged = False
        self.__bombs_around = 0

    def getHasBomb(self):
        return self.__hasBomb
    
    @property
    def bomb(self):
        return self.__hasBomb

    @property
    def clicked(self):
        return self.__clicked
    
    @property
    def flagged(self):
        return self.__flagged
    
    @property
    def bombsAround(self):
        return self.__bombs_around

    def setNeighbors(self, neighbors):
        self.__neighbors = neighbors
        self.setBombsAround()

    def setBombsAround(self):
        self.__bombs_around = 0
        for neighbor in self.__neighbors:
            if (neighbor.getHasBomb()):
                self.__bombs_around += 1

    