import pygame
import sys
from game_elements.inventory import Inventory
from game_elements.item import Item
import subprocess

from game_elements.mystery import Mystery

pygame.init()
pygame.font.init()
# Ustawienia okna
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tajemnicza Gra")

# Kolory
DARK_GRAY = (20, 20, 20)
HIGHLIGHT = (100, 100, 255)

# Ładowanie grafik
background = pygame.image.load("assets/background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

#testowa ikona ekwipunku
equipment_image = pygame.image.load("assets/equipment.jpg").convert_alpha()
equipment_icon_image = pygame.transform.scale(equipment_image, (100, 100))
equipment = equipment_icon_image.get_rect(topleft=(10, 10))

#Testowa ikona kółka i krzyrzyk
tictactoe_image = pygame.image.load("assets/kolko_krzyzyk_icon.jpg").convert_alpha()
tictactoe_image.set_alpha(0)
tictactoe_icon_image = pygame.transform.scale(tictactoe_image, (225, 125))
tictactoe = tictactoe_icon_image.get_rect(midbottom=(WIDTH // 3.2, HEIGHT - 7))

#Testowa ikona klucza nr 1
key_1_image = pygame.image.load("assets/key.jpg").convert_alpha()
key_1_image.set_alpha(250)
key_1_icon_image = pygame.transform.scale(key_1_image, (100, 100))
key_1 = key_1_icon_image.get_rect(midbottom=(WIDTH // 3.2, HEIGHT - 7))

# Skala ikon
icon_size = (100, 100)





def handle_click():
    mouse_pos = pygame.mouse.get_pos()

def open_tictactoe():
    tictactoe_result = subprocess.run(['python', 'minigames/tictactoe/game.py'])
    return tictactoe_result

def main():
    tictactoe_mystery = Mystery('tictactoe')
    key_1_item = Item("Klucz", "assets/key.jpg")
    clock = pygame.time.Clock()
    inv = Inventory()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_click()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # otwieranie ekwipunku
                if equipment.collidepoint(event.pos):
                    inv.toggle()
                # otwieranie minigry tictactoe
                elif tictactoe.collidepoint(event.pos) and tictactoe_mystery.get_status() == False:
                    tictactoe_result = open_tictactoe()
                    if tictactoe_result.returncode == 1:
                        tictactoe_mystery.set_as_completed()
                    tictactoe_mystery.get_status()
                elif key_1.collidepoint(event.pos) and tictactoe_mystery.get_status() == True and inv.if_in_inventory(key_1_item) == False:
                    inv.add_item(key_1_item)

        SCREEN.blit(background, (0, 0))  # Rysuj tło
        SCREEN.blit(equipment_icon_image, equipment)  # Rysuj ikonę ekwipunku
        if tictactoe_mystery.get_status() == False:
            SCREEN.blit(tictactoe_icon_image, tictactoe)

        if tictactoe_mystery.get_status() == True and inv.if_in_inventory(key_1_item) == False:
            SCREEN.blit(key_1_icon_image, key_1)

        if inv.open:
            inv.draw(SCREEN)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()