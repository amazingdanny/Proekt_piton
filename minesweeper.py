import pygame
import os
from board import Board
from piece import Piece
from time import sleep
pygame.init()
font = pygame.font.SysFont('arial',25)

class Minesweeper():
    def __init__(self,board : Board, screen_size):
        self.__board = board
        self.__screen_size = screen_size
        self.__pieceSize = self.__screen_size[0] // self.__board.size[1], self.__screen_size[1] // self.__board.size[0] 
        self.__font = pygame.font.SysFont('arial',25)
        self.loadImages()

    def run(self):
        pygame.init()
        self.__screen = pygame.display.set_mode(self.__screen_size)
        self.__screen_size = (800, 800)
        menu_options = ["Easy", "Medium", "Hard"]
        selected_option = 0

        # menu_running = True
        # while menu_running:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             menu_running = False
        #         elif event.type == pygame.KEYDOWN:
        #             if event.key == pygame.K_UP:
        #                 if selected_option == 1 or 2 or 3:
        #                     selected_option = (selected_option - 1)
        #                 elif selected_option == 0:
        #                     selected_option = 3
        #             elif event.key == pygame.K_DOWN:
        #                 if selected_option == 0 or 1 or 2:
        #                     selected_option = (selected_option + 1)
        #                 elif selected_option == 3:
        #                     selected_option == 0
        #             elif event.key == pygame.K_RETURN:
        #                 menu_running = False
        #     self.__screen.fill((0, 0, 0))
        #     for i, option in enumerate(menu_options):
        #         text_color = (255, 255, 255) 
        #         if i == selected_option:
        #             text_color = (255, 255, 0) 

        #         self.__text = self.__font.render(str(option), True, text_color)
        #         text_width, text_height = self.__text.get_size()
        #         text_x = (self.__screen_size[0] - text_width) // 2
        #         text_y = (self.__screen_size[1] // 2) + (i - len(menu_options) // 2) * text_height * 2

        #         self.__screen.blit(self.__text, (text_x, text_y))
        #     pygame.display.flip()
        #     if selected_option == 0: 
        #         board_size = (9, 9)
        #         self.__screen_size = (800, 800)
        #     elif selected_option == 1:  
        #         board_size = (16, 16)
        #         self._screen_size = (1200, 1200)
        #     elif selected_option == 3:  
        #         board_size = (24, 24)
        #         self.__screen_size = (1600, 1600)
        #     self.__board = Board(board_size, 0.1)
            
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(position, rightClick)
                if event.type == pygame.KEYDOWN and self.__board.getLost():
                        self.__board.replay()
                        self.__board.setBoard()
                        self.draw()
                if event.type == pygame.KEYDOWN and self.__board.getWon():
                    self.__board.replay()
                    self.__board.setBoard()
                    self.draw()
            self.draw()
            pygame.display.flip()
            if self.__board.getWon():
                font = pygame.font.Font(None, 128)
                text = font.render(r"You Won!!!\n Press any key to restart", True, (255, 0, 0))
                text_width, text_height = text.get_size()
                text_x = (self.__screen_size[0] - text_width) // 2
                text_y = (self.__screen_size[1] - text_height) // 2
                self.__screen.blit(text, (text_x, text_y))
                pygame.display.flip()
            if self.__board.getLost():
                font = pygame.font.Font(None, 128)
                text = font.render("You Lost \n press any key to restart", True, (255, 0, 0))
                text_width, text_height = text.get_size()
                text_x = (self.__screen_size[0] - text_width) // 2
                text_y = (self.__screen_size[1] - text_height) // 2
                self.__screen.blit(text, (text_x, text_y))
                pygame.display.flip()
        pygame.quit()
        
    #def draw_menu(self):

    
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

    #def click_menu(self):
