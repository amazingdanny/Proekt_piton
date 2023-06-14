from minesweeper import Minesweeper
from board import Board
import pygame

pygame.init()
size = (800, 800)
screen = pygame.display.set_mode(size)
screen_size = (800, 800)
menu_options = ["Easy", "Medium", "Hard"]
selected_option = 0
font = pygame.font.SysFont('arial',25)

menu_running = True
while menu_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(menu_options)
            elif event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(menu_options)
            elif event.key == pygame.K_RETURN:
                menu_running = False

    screen.fill((0, 0, 0))
    max_text_width = max(font.size(option)[0] for option in menu_options)
    max_text_height = max(font.size(option)[1] for option in menu_options)
    center_x = screen_size[0] // 2
    center_y = screen_size[1] // 2
    menu_height = len(menu_options) * (max_text_height + 10)
    start_y = center_y - menu_height // 2

    for i, option in enumerate(menu_options):
        text_color = (255, 255, 255)
        if i == selected_option:
            text_color = (255, 255, 0)

        text = font.render(str(option), True, text_color)
        text_width, text_height = text.get_size()
        text_x = center_x - text_width // 2
        text_y = start_y + i * (text_height + 10)

        screen.blit(text, (text_x, text_y))

    pygame.display.flip()

    if selected_option == 0: 
        board_size = (9, 9)
        screen_size = (800, 800)
    elif selected_option == 1:  
        board_size = (16, 16)
        screen_size = (900, 800)
    elif selected_option == 3:  
        board_size = (24, 24)
        screen_size = (1000, 800)
    board = Board(board_size, 0.1)

size = (8, 8)

scsize = (800, 800)
game = Minesweeper(board, screen_size)
game.run() 