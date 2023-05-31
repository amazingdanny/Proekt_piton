import pygame
import os
from board import Board
from piece import Piece
from time import sleep

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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(position, rightClick)
            self.draw()
            pygame.display.flip()
            if self.__board.getWon():
                font = pygame.font.Font(None, 128)
                text = font.render("You Won!!!", True, (255, 0, 0))
                text_width, text_height = text.get_size()
                text_x = (self.__screen_size[0] - text_width) // 2
                text_y = (self.__screen_size[1] - text_height) // 2
                self.__screen.blit(text, (text_x, text_y))
                pygame.display.flip()
            if self.__board.getLost():
                font = pygame.font.Font(None, 128)
                text = font.render("You Lost", True, (255, 0, 0))
                text_width, text_height = text.get_size()
                text_x = (self.__screen_size[0] - text_width) // 2
                text_y = (self.__screen_size[1] - text_height) // 2
                self.__screen.blit(text, (text_x, text_y))
                pygame.display.flip()
        pygame.quit()
        
            
    
    def draw(self):
        topLeft = (0, 0)
        for row in range(self.__board.size[0]):
            for col in range(self.__board.size[1]):
                piece = self.__board.getPiece((row, col))
                image = self.getImage(piece)
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
        
    def getImage(self, piece: Piece):
        string = ""
        if piece.clicked:
            string = "bomb-at-clicked-block" if piece.bomb else str(piece.bombsAround)
        else:
            string = "flag" if piece.flagged else "empty-block"
        return self.__images[string]
    
    def handleClick(self, position, rightClick):
        index = position[1] // self.__pieceSize[1], position[0] // self.__pieceSize[0]
        piece = self.__board.getPiece(index)
        self.__board.handleClick(piece, rightClick)