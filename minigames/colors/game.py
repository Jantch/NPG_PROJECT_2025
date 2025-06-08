import pygame, sys, random, os

# --- Inicjalizacja Pygame ---
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("Puzzle 3x3 z ramką")
clock = pygame.time.Clock()

# --- Kolory kwadratów ---
RED     = (255,   0,   0)
GREEN   = (  0, 255,   0)
BLUE    = (  0,   0, 255)
YELLOW  = (255, 255,   0)
ORANGE  = (255, 165,   0)
PURPLE  = (128,   0, 128)
CYAN    = (  0, 255, 255)
MAGENTA = (255,   0, 255)
BROWN   = (165,  42,  42)
colors = [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN, MAGENTA, BROWN]

# Docelowy układ kolorów (po wierszach)
target_order = colors.copy()

# Losowy początkowy układ różny od docelowego
def shuffled_colors():
    arr = colors.copy()
    random.shuffle(arr)
    return arr
initial_colors = shuffled_colors()
while initial_colors == target_order:
    initial_colors = shuffled_colors()

# --- Wczytanie ramki z pełnym wsparciem alfa ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(SCRIPT_DIR, "static")
frame_path = os.path.join(IMAGE_DIR, "frame.png")
frame_img = pygame.image.load(frame_path).convert_alpha()
# Skaluje ramkę do wymiarów całego ekranu
frame_img = pygame.transform.smoothscale(frame_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

#Wczytanie dźwięków
BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BASE_PATH_SOUNDS = os.path.join(BASE_PATH, "sounds", "effects")
move_sound = pygame.mixer.Sound(os.path.join(BASE_PATH_SOUNDS, "colors_sound.wav"))
place_sound = pygame.mixer.Sound(os.path.join(BASE_PATH_SOUNDS, "tictactoe_click.wav"))
place_sound.set_volume(0.3)

# Margines wewnątrz ramki i rozmiar pól w pikselach
FRAME_BORDER = 39
INNER_SIZE = SCREEN_WIDTH - 2 * FRAME_BORDER
CELL_SIZE = INNER_SIZE // 3

class Square:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        # Pozycja wewnątrz ramki
        self.rect = pygame.Rect(
            FRAME_BORDER + col * CELL_SIZE,
            FRAME_BORDER + row * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE
        )
        self.dragging = False

    def draw(self, surface):
        # Rysujemy kolorowy kwadrat
        pygame.draw.rect(surface, self.color, self.rect)

# Tworzymy obiekty Square
squares = []
for idx, color in enumerate(initial_colors):
    r, c = divmod(idx, 3)
    squares.append(Square(r, c, color))

font = pygame.font.SysFont(None, 36)
running = True
selected = None
offset_x = offset_y = 0

while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

        elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
            for sq in squares:
                if sq.rect.collidepoint(ev.pos):
                    selected = sq
                    sq.dragging = True
                    mx, my = ev.pos
                    offset_x = sq.rect.x - mx
                    offset_y = sq.rect.y - my
                    move_sound.play()  #PODNIESIENIE
                    break

        elif ev.type == pygame.MOUSEBUTTONUP and selected:
            selected.dragging = False
            mx, my = ev.pos
            # Wyznacz pole docelowe względem ramki
            tx = (mx - FRAME_BORDER) // CELL_SIZE
            ty = (my - FRAME_BORDER) // CELL_SIZE
            if 0 <= ty < 3 and 0 <= tx < 3:
                for other in squares:
                    if other is not selected and other.row == ty and other.col == tx:
                        # Zamiana pozycji
                        selected.row, other.row = other.row, selected.row
                        selected.col, other.col = other.col, selected.col
                        other.rect.topleft = (
                            FRAME_BORDER + other.col * CELL_SIZE,
                            FRAME_BORDER + other.row * CELL_SIZE
                        )
                        place_sound.play()  #ZAMIANA
                        break
            # Przywracamy wybrany kwadrat na aktualne pole
            selected.rect.topleft = (
                FRAME_BORDER + selected.col * CELL_SIZE,
                FRAME_BORDER + selected.row * CELL_SIZE
            )
            selected = None

        elif ev.type == pygame.MOUSEMOTION and selected and selected.dragging:
            mx, my = ev.pos
            selected.rect.x = mx + offset_x
            selected.rect.y = my + offset_y

    # Rysowanie tła i ramki
    screen.fill((255, 255, 255))
    screen.blit(frame_img, (0, 0))
    # Rysowanie kwadratów wewnątrz ramki
    for sq in squares:
        sq.draw(screen)

    # Opcjonalne linie siatki wewnątrz ramki
    line_color = (0, 0, 0)
    for i in range(1, 3):
        x = FRAME_BORDER + i * CELL_SIZE
        y = FRAME_BORDER + i * CELL_SIZE
        pygame.draw.line(screen, line_color, (x, FRAME_BORDER), (x, SCREEN_HEIGHT - FRAME_BORDER), 2)
        pygame.draw.line(screen, line_color, (FRAME_BORDER, y), (SCREEN_WIDTH - FRAME_BORDER, y), 2)

    # Sprawdzenie poprawności ułożenia
    solved = True
    for sq in squares:
        idx = sq.row * 3 + sq.col
        if sq.color is not target_order[idx]:
            solved = False
            break

    if solved:
        msg = font.render("Gratulacje!", True, (0, 0, 0))
        rect = msg.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        screen.blit(msg, rect)
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit(solved)
