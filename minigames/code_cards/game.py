import os
import pygame
import sys

pygame.init()
def load_background(filename):
    base_path = os.path.dirname(__file__)  # folder, w którym jest game.py (czyli minigra)
    path = os.path.join(base_path, "static", filename)
    return pygame.image.load(path).convert()

def load_and_scale_digit_images(folder, digits, max_width):
    digit_images = []
    base_path = os.path.dirname(__file__)
    for digit in digits:
        path = os.path.join(base_path, folder, f"{digit}.jpg")
        img = pygame.image.load(path).convert_alpha()
        scale_factor = max_width / img.get_width()
        new_width = int(img.get_width() * scale_factor)
        new_height = int(img.get_height() * scale_factor)
        scaled_img = pygame.transform.smoothscale(img, (new_width, new_height))
        digit_images.append(scaled_img)
    return digit_images

    return digit_images



# Ustawienia ekranu
WIDTH, HEIGHT = 245, 372
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kod 4-cyfrowy")

# Wczytanie tła
background = load_background("cards_numbers_background.jpg")

# Wczytanie obrazków cyfr
max_digit_width = 31
digit_images = load_and_scale_digit_images("static", range(0, 10), max_digit_width)

# Rozmiar jednego przycisku
digit_width, digit_height = digit_images[0].get_size()

# Pozycje przycisków na ekranie
digit_positions = [(58 + i * (digit_width), 270) for i in range(4)]

# Obecny kod
code = [2, 5, 8, 0]

# Tworzymy prostokąty przycisków (dla kliknięć)
digit_rects = [pygame.Rect(x, y, digit_width, digit_height) for x, y in digit_positions]

def check_code(player_code, correct_code=[2, 1, 3, 7]):
    return player_code == correct_code

# Główna pętla gry
result = 0
running = True
while running:

    SCREEN.blit(background, (0, 0))

    # Rysowanie cyfr
    for i in range(4):
        img = digit_images[code[i]]
        SCREEN.blit(img, digit_positions[i])

    pygame.display.flip()

    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit(result)

        elif event.type == pygame.MOUSEBUTTONDOWN and result == 0:
            pos = event.pos
            for i, rect in enumerate(digit_rects):
                if rect.collidepoint(pos):
                    code[i] += 1
                    if code[i] > 9:
                        code[i] = 0

        if check_code(code) and result == 0:
            #print("Brawo! Kod poprawny!")
            result = 1
            #print(result)


pygame.quit()
sys.exit(result)