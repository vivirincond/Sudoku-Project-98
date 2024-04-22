import pygame
import sys
from board import Board
from cell import *
from constants import *
from sudoku_generator import *


def game_start_screen():
    game_over = False
    # Sets the background to white
    screen.fill(WHITE)

    # Title
    title_font = pygame.font.Font(None, 64)
    title_text = title_font.render("Welcome to Sudoku", True, BLACK)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(title_text, title_rect)

    # Displays "Select Game Mode:"
    mode_font = pygame.font.Font(None, 32)
    mode_text = mode_font.render("Select Game Mode:", True, BLACK)
    mode_rect = mode_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(mode_text, mode_rect)

    # Creates easy, medium, and hard buttons
    #EASY BUTTON:
    button_font = pygame.font.Font(None, 32)
    easy_button = button_font.render("Easy", True, BLACK)
    easy_surface=pygame.Surface((easy_button.get_size()[0]+20, easy_button.get_size()[1]+20))
    easy_surface.fill((255,100,180))
    easy_surface.blit(easy_button,(10,10))
    easy_rect = easy_button.get_rect(center=(WIDTH // 4, HEIGHT * 3 // 4))
    screen.blit(easy_surface, easy_rect)
    #MEDIUM BUTTON:
    medium_button = button_font.render("Medium", True, BLACK)
    medium_surface=pygame.Surface((medium_button.get_size()[0]+20, medium_button.get_size()[1]+20))
    medium_surface.fill((255,0,230))
    medium_surface.blit(medium_button,(10,10))
    medium_rect = medium_button.get_rect(center=(WIDTH // 2, HEIGHT * 3 // 4))
    screen.blit(medium_surface, medium_rect)
    #HARD BUTTON:
    hard_button = button_font.render("Hard", True, BLACK)
    hard_surface=pygame.Surface((hard_button.get_size()[0]+20, hard_button.get_size()[1]+20))
    hard_surface.fill((220,0,255))
    hard_surface.blit(hard_button,(10,10))
    hard_rect = hard_button.get_rect(center=(WIDTH * 3 // 4, HEIGHT * 3 // 4))
    screen.blit(hard_surface, hard_rect)


#     game_over_font = pygame.font.Font(None, GAME_OVER_FONT)

#def main_menu():#main menu screen
    #pygame.init()
    #screen = pygame.display.set_mode((WIDTH, HEIGHT))
    #.display.set_caption("SUDOKU")
    #game_over_font = pygame.font.Font(None, GAME_OVER_FONT)
    #game_over = False

    # screen.fill(BG_COLOR)
    # b = Board(2, 2, screen, 1)
    # b.draw()
    # c = Cell(1, 8, 0, screen)
    # c.draw()

    #Creates instance of board class in order to call board methods.
    b = Board(2, 2, screen, 1)

    #Creates instance of cell class in order to call cell methods
    c = Cell(1, 8, 0, screen)
    #Start screen where the Easy, Medium and Hard buttons are placed
    while True:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN and not game_over:
                if easy_rect.collidepoint(event.pos):
                    easy_screen()
                if medium_rect.collidepoint(event.pos):
                    medium_screen()
                if hard_rect.collidepoint(event.pos):
                    hard_screen()

            if event.type == pygame.MOUSEBUTTONDOWN:
                c.touch=True
                x, y = event.pos
                row = y // SQUARE_SIZE
                col = (x // SQUARE_SIZE)

        # Clear the screen
        #screen.fill((0, 0, 0))

        pygame.display.update()

# def game_in_progress():
#     reset_font = pygame.font.Font(None, 32)
#     reset_button = reset_font.render("Reset", True, BLACK)
#     reset_rect = reset_button.get_rect(center=(WIDTH // 4, HEIGHT * 2.55 // 2.8))
#     restart_font=pygame.font.Font(None,32)
#     restart_button = restart_font.render("Restart", True, BLACK)
#     restart_rect = restart_button.get_rect(center=(WIDTH // 2, HEIGHT * 2.55 // 2.8))
#     exit_button = reset_font.render("Exit", True, BLACK)
#     exit_rect = exit_button.get_rect(center=(WIDTH * 3 // 4, HEIGHT * 2.55 // 2.8))
#
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if restart_rect.collidepoint(event.pos):
#                     game_start_screen()
#                 if exit_rect.collidepoint(event.pos):
#                     sys.exit()
#     pass
#

def easy_screen():
    screen.fill(BG_COLOR)

    b = Board(2, 2, screen, 1)
    b.draw()
    #Buttons
    reset_font = pygame.font.Font(None, 32)
    reset_button = reset_font.render("Reset", True, BLACK)
    reset_surface = pygame.Surface((reset_button.get_size()[0] + 20, reset_button.get_size()[1] + 20))
    reset_surface.fill(EASY_COLOR)
    reset_surface.blit(reset_button, (10, 10))
    reset_rect = reset_button.get_rect(center=(WIDTH // 4, HEIGHT * 2.55 // 2.8))
    screen.blit(reset_surface, reset_rect)

    restart_font=pygame.font.Font(None,32)
    restart_button = restart_font.render("Restart", True, BLACK)
    restart_surface = pygame.Surface((restart_button.get_size()[0] + 20, restart_button.get_size()[1] + 20))
    restart_surface.fill(EASY_COLOR)
    restart_surface.blit(restart_button, (10, 10))
    restart_rect = restart_button.get_rect(center=(WIDTH // 2, HEIGHT * 2.55 // 2.8))
    screen.blit(restart_surface, restart_rect)


    exit_button = reset_font.render("Exit", True, BLACK)
    exit_surface = pygame.Surface((exit_button.get_size()[0] + 20, exit_button.get_size()[1] + 20))
    exit_surface.fill(EASY_COLOR)
    exit_surface.blit(exit_button, (10, 10))
    exit_rect = exit_button.get_rect(center=(WIDTH * 3 // 4, HEIGHT * 2.55 // 2.8))
    screen.blit(exit_surface, exit_rect)

    z = generate_sudoku(9, 30)


    for j in range(9):
        for i in range(9):
            value = z[i][j]

            c = Cell(value, i, j, screen)
            c.draw()

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.line(screen, BLUE, (0, HEIGHT - 100), (WIDTH, HEIGHT - 100), LINE_WIDTH // 3)
                x, y = event.pos
                row = y // SQUARE_SIZE
                col = x // SQUARE_SIZE


                if restart_rect.collidepoint(event.pos):
                    game_start_screen()
                if exit_rect.collidepoint(event.pos):
                        sys.exit()


def medium_screen():
    screen.fill(BG_COLOR)

    b = Board(2, 2,screen,2)
    b.draw()
    reset_font = pygame.font.Font(None, 32)
    reset_button = reset_font.render("Reset", True, BLACK)
    reset_surface = pygame.Surface((reset_button.get_size()[0] + 20, reset_button.get_size()[1] + 20))
    reset_surface.fill(MEDIUM_COLOR)
    reset_surface.blit(reset_button, (10, 10))
    reset_rect = reset_button.get_rect(center=(WIDTH // 4, HEIGHT * 2.55 // 2.8))
    screen.blit(reset_surface, reset_rect)

    restart_font = pygame.font.Font(None, 32)
    restart_button = restart_font.render("Restart", True, BLACK)
    restart_surface = pygame.Surface((restart_button.get_size()[0] + 20, restart_button.get_size()[1] + 20))
    restart_surface.fill(MEDIUM_COLOR)
    restart_surface.blit(restart_button, (10, 10))
    restart_rect = restart_button.get_rect(center=(WIDTH // 2, HEIGHT * 2.55 // 2.8))
    screen.blit(restart_surface, restart_rect)

    exit_button = reset_font.render("Exit", True, BLACK)
    exit_surface = pygame.Surface((exit_button.get_size()[0] + 20, exit_button.get_size()[1] + 20))
    exit_surface.fill(MEDIUM_COLOR)
    exit_surface.blit(exit_button, (10, 10))
    exit_rect = exit_button.get_rect(center=(WIDTH * 3 // 4, HEIGHT * 2.55 // 2.8))
    screen.blit(exit_surface, exit_rect)
    z = generate_sudoku(9, 40)
    for j in range(9):
        for i in range(9):
            value = z[i][j]
            c = Cell(value, i, j, screen)
            c.draw()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos):
                    game_start_screen()
                if exit_rect.collidepoint(event.pos):
                    sys.exit()

def hard_screen():

    screen.fill(BG_COLOR)

    b = Board(2, 2,screen,2)
    b.draw()
    reset_font = pygame.font.Font(None, 32)
    reset_button = reset_font.render("Reset", True, BLACK)
    reset_surface = pygame.Surface((reset_button.get_size()[0] + 20, reset_button.get_size()[1] + 20))
    reset_surface.fill(HARD_COLOR)
    reset_surface.blit(reset_button, (10, 10))
    reset_rect = reset_button.get_rect(center=(WIDTH // 4, HEIGHT * 2.55 // 2.8))
    screen.blit(reset_surface, reset_rect)

    restart_font = pygame.font.Font(None, 32)
    restart_button = restart_font.render("Restart", True, BLACK)
    restart_surface = pygame.Surface((restart_button.get_size()[0] + 20, restart_button.get_size()[1] + 20))
    restart_surface.fill(HARD_COLOR)
    restart_surface.blit(restart_button, (10, 10))
    restart_rect = restart_button.get_rect(center=(WIDTH // 2, HEIGHT * 2.55 // 2.8))
    screen.blit(restart_surface, restart_rect)

    exit_button = reset_font.render("Exit", True, BLACK)
    exit_surface = pygame.Surface((exit_button.get_size()[0] + 20, exit_button.get_size()[1] + 20))
    exit_surface.fill(HARD_COLOR)
    exit_surface.blit(exit_button, (10, 10))
    exit_rect = exit_button.get_rect(center=(WIDTH * 3 // 4, HEIGHT * 2.55 // 2.8))
    screen.blit(exit_surface, exit_rect)
    z = generate_sudoku(9, 50)
    for j in range(9):
        for i in range(9):
            value = z[i][j]
            c = Cell(value, i, j, screen)
            c.draw()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos):
                    game_start_screen()
                if exit_rect.collidepoint(event.pos):
                    sys.exit()









# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Initialize pygame, set the screen, and go to the start page
    pygame.init()
    pygame.display.set_caption("SUDOKU")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game_start_screen()
