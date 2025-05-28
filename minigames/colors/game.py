import pygame
import sys
import random

# Inicjalizacja Pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Puzzle 3x3 - Przeciągnij, aby zamienić")

# Definicja kolorów RGB
RED    = (255,   0,   0)
GREEN  = (  0, 255,   0)
BLUE   = (  0,   0, 255)
YELLOW = (255, 255,   0)
ORANGE = (255, 165,   0)
PURPLE = (128,   0, 128)
CYAN   = (  0, 255, 255)
MAGENTA= (255,   0, 255)
BROWN  = (165,  42,  42)

colors = [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN, MAGENTA, BROWN]

# Docelowy układ kolorów: lista 9 kolorów (kolejno po wierszach)
target_order = [
    RED, GREEN, BLUE,
    YELLOW, ORANGE, PURPLE,
    CYAN, MAGENTA, BROWN
]

# Losowy początkowy układ, różny od docelowego
initial_colors = colors.copy()
random.shuffle(initial_colors)
while initial_colors == target_order:
    random.shuffle(initial_colors)

cell_size = SCREEN_WIDTH // 3  # Rozmiar każdego kwadratu: 100x100 pikseli

class Square:
    def __init__(self, row, col, color):
        # Współrzędne w siatce (wiersz, kolumna) i przypisany kolor
        self.row = row
        self.col = col
        self.color = color
        # Prostokąt do rysowania: umieszczony początkowo na podstawie (row, col)
        self.rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
        self.dragging = False  # flaga przeciągania

    def draw(self, surface):
        # Rysujemy kolorowy kwadrat w miejscu prostokąta
        pygame.draw.rect(surface, self.color, self.rect)

# Tworzymy listę kwadratów według początkowego układu kolorów
squares = []
for index, color in enumerate(initial_colors):
    row = index // 3
    col = index % 3
    square = Square(row, col, color)
    squares.append(square)

font = pygame.font.SysFont(None, 36)  # Czcionka do komunikatu końcowego

running = True
selected_square = None
offset_x = offset_y = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Kliknięcie myszy
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for square in squares:
                if square.rect.collidepoint(event.pos):
                    selected_square = square
                    square.dragging = True
                    mouse_x, mouse_y = event.pos
                    # Obliczamy przesunięcie między położeniem prostokąta a kursorem
                    offset_x = square.rect.x - mouse_x
                    offset_y = square.rect.y - mouse_y
                    break

        # Zwolnienie przycisku myszy
        elif event.type == pygame.MOUSEBUTTONUP and selected_square:
            selected_square.dragging = False

            # 1) Wyznacz pole docelowe na podstawie pozycji kursora
            mouse_x, mouse_y = event.pos
            target_col = mouse_x // cell_size
            target_row = mouse_y // cell_size

            # 2) Jeżeli to pole jest w siatce, znajdź kwadrat o tych współrzędnych
            if 0 <= target_row < 3 and 0 <= target_col < 3:
                for other in squares:
                    if other.row == target_row and other.col == target_col \
                            and other is not selected_square:
                        # 3) Zamień ich row i col
                        selected_square.row, other.row = other.row, selected_square.row
                        selected_square.col, other.col = other.col, selected_square.col
                        # 4) Zaktualizuj ich recty
                        other.rect.topleft = (other.col * cell_size, other.row * cell_size)
                        break

            # 5) Na koniec zawsze “wskakujemy” przeciągany kwadrat na swoje pole
            selected_square.rect.topleft = (
                selected_square.col * cell_size,
                selected_square.row * cell_size
            )
            selected_square = None

        # Ruch myszy (ciągnięcie)
        elif event.type == pygame.MOUSEMOTION:
            if selected_square and selected_square.dragging:
                mouse_x, mouse_y = event.pos
                selected_square.rect.x = mouse_x + offset_x
                selected_square.rect.y = mouse_y + offset_y

    # Rysujemy tło i siatkę
    screen.fill((255, 255, 255))  # białe tło
    # Rysujemy wszystkie kwadraty
    for square in squares:
        square.draw(screen)
    # Rysujemy obramowanie - linie siatki
    line_color = (0, 0, 0)
    for i in range(1, 3):
        # pionowa linia
        pygame.draw.line(screen, line_color, (i * cell_size, 0), (i * cell_size, SCREEN_HEIGHT), 2)
        # pozioma linia
        pygame.draw.line(screen, line_color, (0, i * cell_size), (SCREEN_WIDTH, i * cell_size), 2)

    # Sprawdzamy, czy ułożono poprawny wzór
    solved = True
    for square in squares:
        index = square.row * 3 + square.col
        if square.color != target_order[index]:
            solved = False
            break

    if solved:
        # Wyświetlamy komunikat i kończymy grę po chwili
        text = font.render("Gratulacje, ułożyłeś wzór!", True, (0, 0, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(3000)  # pauza 3 sekundy
        running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
