import pygame
import random
import sys
import os

# --- USTAWIENIA GRY ---
pygame.init()
WIDTH, HEIGHT = 800, 800

# obszar rysowanej planszy wewnątrz ramki w tle
BOARD_X = 100
BOARD_Y = 100
BOARD_W = WIDTH  - 2*BOARD_X
BOARD_H = HEIGHT - 2*BOARD_Y
CELL    = BOARD_W // 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kółko i Krzyżyk")

FONT = pygame.font.SysFont(None, 36)

# skala i ewentualne drobne przesunięcia
SYMBOL_SCALE   = 0.5
SYMBOL_OFFSETS = {'X': (0, 0), 'O': (0, 0)}

# ścieżki do plików
BASE_PATH        = os.path.dirname(__file__)
BACKGROUND_PATH  = os.path.join(BASE_PATH, "static", "image.png")
O_IMG_PATH       = os.path.join(BASE_PATH, "static", "circle.png")
X_IMG_PATH       = os.path.join(BASE_PATH, "static", "cross.png")

# --- ŁADOWANIE ZASOBÓW ---
# tło
background = pygame.image.load(BACKGROUND_PATH).convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# symbole
symbol_size = int(CELL * SYMBOL_SCALE)

o_img = pygame.image.load(O_IMG_PATH).convert_alpha()
o_img = pygame.transform.scale(o_img, (symbol_size, symbol_size))

x_img = pygame.image.load(X_IMG_PATH).convert_alpha()
x_img = pygame.transform.scale(x_img, (symbol_size, symbol_size))

# --- STAN GRY ---
board                = [[None]*3 for _ in range(3)]
game_over, winner    = False, None
draw_flag            = False

# dla opóźnienia ruchu komputera
COMPUTER_DELAY       = 1000  # ms
pending_computer_move = False
computer_move_time    = 0
computer_move_pos     = None

def draw_board():
    screen.blit(background, (0, 0))
    for row in range(3):
        for col in range(3):
            sym = board[row][col]
            if sym in ('X','O'):
                icon = x_img if sym=='X' else o_img
                rect = icon.get_rect()
                rect.center = (
                    BOARD_X + col*CELL + CELL//2 + SYMBOL_OFFSETS[sym][0],
                    BOARD_Y + row*CELL + CELL//2 + SYMBOL_OFFSETS[sym][1]
                )
                screen.blit(icon, rect)

def check_winner():
    global winner, draw_flag, game_over
    # wiersze/kolumny
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]!=None:
            winner = board[i][0]; game_over = True; return
        if board[0][i]==board[1][i]==board[2][i]!=None:
            winner = board[0][i]; game_over = True; return
    # przekątne
    if board[0][0]==board[1][1]==board[2][2]!=None:
        winner = board[0][0]; game_over = True; return
    if board[0][2]==board[1][1]==board[2][0]!=None:
        winner = board[0][2]; game_over = True; return
    # remis
    if all(board[r][c] is not None for r in range(3) for c in range(3)):
        draw_flag = True
        game_over = True
waiting = False
# --- GŁÓWNA PĘTLA ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ruch gracza
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if waiting:
                continue
            mx, my = event.pos
            # sprawdź kliknięcie wewnątrz planszy
            if BOARD_X <= mx < BOARD_X+BOARD_W and BOARD_Y <= my < BOARD_Y+BOARD_H:
                col = (mx - BOARD_X) // CELL
                row = (my - BOARD_Y) // CELL
                if board[row][col] is None:
                    board[row][col] = 'X'
                    check_winner()
                    if not game_over:
                        # zaplanuj ruch komputera
                        empty = [(r,c) for r in range(3) for c in range(3) if board[r][c] is None]
                        if empty:
                            pending_computer_move = True
                            computer_move_time    = pygame.time.get_ticks()
                            computer_move_pos     = random.choice(empty)

        # restart
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            board[:]             = [[None]*3 for _ in range(3)]
            game_over, winner    = False, None
            draw_flag            = False
            pending_computer_move = False
            computer_move_pos     = None

    # opóźniony ruch komputera
    if pending_computer_move and not game_over:
        waiting = True
        if pygame.time.get_ticks() - computer_move_time >= COMPUTER_DELAY:
            r, c = computer_move_pos
            board[r][c] = 'O'
            check_winner()
            pending_computer_move = False
            computer_move_pos     = None
            waiting = False

    # rysuj i wyświetl komunikat końcowy
    draw_board()
    if game_over:
        # 1) przyciemnij cały ekran
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)  # Surface z alpha
        overlay.fill((0, 0, 0, 180))  # czarne tło z alpha=180/255
        screen.blit(overlay, (0, 0))

        # 2) przygotuj własną czcionkę i kolor tekstu
        end_font = pygame.font.SysFont("arial", 50, bold=True)
        # zmień treść na dowolną:
        if winner == 'X':
            msg = "Trafiłeś! Krzyżyk wygrywa!"
        elif winner == 'O':
            msg = "Komputer wygrywa..."
        else:
            msg = "Remis! Spróbuj jeszcze raz."
        # renderuj biały tekst ze cieniem
        text = end_font.render(msg, True, (255, 255, 255))
        # dla lepszego kontrastu zrób cień:
        shadow = end_font.render(msg, True, (0, 0, 0))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        shadow_rect = text_rect.copy()
        shadow_rect.move_ip(2, 2)

        screen.blit(shadow, shadow_rect)
        screen.blit(text, text_rect)



    pygame.display.flip()

pygame.quit()
sys.exit()
