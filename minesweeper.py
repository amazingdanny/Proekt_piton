import pygame
import os
from board import Board

class Minesweeper():
    def __init__(self,board : Board,screen_size):
        self.__board = board
        self.__screen_size = screen_size
        self.__pieceSize = self.__screen_size[0] // self.__board.size[1], self.__screen_size[1] // self.__board.size[0] 
        self.loadImages()

    def run(self):
        pygame.init()
        self.__screen = pygame.display.set_mode(self.__screen_size)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw()
            pygame.display.flip()
        pygame.quit()
    
    def draw(self):
        topLeft = (0, 0)
        for row in range(self.__board.size[0]):
            for col in range(self.__board.size[1]):
                image = self.__images["empty-block"]
                self.__screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.__pieceSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.__pieceSize[1] 

    def loadImages(self):
        self.__images = {}
        for filename in os.listdir("images"):
            if not filename.endswith(".png"):
                continue
            image = pygame.image.load(r"images/" + filename)
            image = pygame.transform.scale(image, self.__pieceSize)
            self.__images[filename.split(".")[0]] = image 