import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 300, 300
CELL = WIDTH // 3
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kółko i Krzyżyk")
FONT = pygame.font.SysFont(None, 36)
LINE_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)

board = [[None for _ in range(3)] for _ in range(3)]
game_over = False
winner = None
draw = False

def draw_board():
    screen.fill(BG_COLOR)
    # Rysowanie linii siatki
    pygame.draw.line(screen, LINE_COLOR, (CELL, 0), (CELL, HEIGHT), 2)
    pygame.draw.line(screen, LINE_COLOR, (2*CELL, 0), (2*CELL, HEIGHT), 2)
    pygame.draw.line(screen, LINE_COLOR, (0, CELL), (WIDTH, CELL), 2)
    pygame.draw.line(screen, LINE_COLOR, (0, 2*CELL), (WIDTH, 2*CELL), 2)
    # Rysowanie symboli X i O
    for row in range(3):
        for col in range(3):
            symbol = board[row][col]
            if symbol == 'X':
                # Krzyżyk: dwie przekątne
                start_x = col*CELL + 5;   start_y = row*CELL + 5
                end_x   = col*CELL + CELL - 5; end_y   = row*CELL + CELL - 5
                pygame.draw.line(screen, LINE_COLOR, (start_x, start_y), (end_x, end_y), 2)
                pygame.draw.line(screen, LINE_COLOR, (start_x, end_y),   (end_x, start_y), 2)
            elif symbol == 'O':
                # Kółko: okrąg
                center_x = col*CELL + CELL//2
                center_y = row*CELL + CELL//2
                radius = CELL//2 - 5
                pygame.draw.circle(screen, LINE_COLOR, (center_x, center_y), radius, 2)

def check_winner():
    global winner, draw, game_over
    # Sprawdzenie zwycięstwa
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != None:
            winner = board[i][0]; game_over = True; return
        if board[0][i] == board[1][i] == board[2][i] != None:
            winner = board[0][i]; game_over = True; return
    if board[0][0] == board[1][1] == board[2][2] != None:
        winner = board[0][0]; game_over = True; return
    if board[0][2] == board[1][1] == board[2][0] != None:
        winner = board[0][2]; game_over = True; return
    # Sprawdzenie remisu (brak pustych pól)
    if all(board[r][c] is not None for r in range(3) for c in range(3)):
        draw = True; game_over = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Ruch gracza (kliknięcie myszą)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            row = y // CELL
            col = x // CELL
            if board[row][col] is None:
                board[row][col] = 'X'
                check_winner()
                if not game_over:
                      # 1 sekunda opóźnienia
                    # Ruch losowy komputera
                    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] is None]
                    if empty_cells:
                        r, c = random.choice(empty_cells)
                        board[r][c] = 'O'
                    check_winner()

        # Restart gry po naciśnięciu 'R'
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                board = [[None for _ in range(3)] for _ in range(3)]
                game_over = False
                winner = None
                draw = False

    draw_board()
    # Wyświetlenie komunikatu po zakończeniu gry
    if game_over:
        if winner == 'X':
            msg = "Krzyżyk wygrał!"
        elif winner == 'O':
            msg = "Kółko wygrało!"
        else:
            msg = "Remis!"
        text = FONT.render(msg, True, (10, 10, 10))
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
