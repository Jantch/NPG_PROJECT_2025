import pygame
import sys
from templates.inventory import Inventory
from templates.item import Item
import subprocess

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

#Ikona ekwipunku
equipment_image = pygame.image.load("assets/equipment.jpg").convert_alpha()
equipment_icon_image = pygame.transform.scale(equipment_image, (100, 100))
equipment = equipment_icon_image.get_rect(topleft=(10, 10))

#Testowa ikona kółka i krzyrzyk
tictactoe_image = pygame.image.load("assets/kolko_krzyzyk_icon.jpg").convert_alpha()
tictactoe_icon_image = pygame.transform.scale(tictactoe_image, (100, 100))
tictactoe = tictactoe_icon_image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 10))

# Skala ikon
icon_size = (100, 100)





def handle_click():
    mouse_pos = pygame.mouse.get_pos()

def open_tictactoe():
    subprocess.Popen(['python', 'minigames/tictactoe/game.py'])


def main():
    key_item = Item("Klucz", "assets/key.jpg")
    clock = pygame.time.Clock()
    inv = Inventory()
    inv.add_item(key_item)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #handle_click()


        #otwieranie ekwipunku
            if event.type == pygame.MOUSEBUTTONDOWN:
                if equipment.collidepoint(event.pos):
                    inv.toggle()

                if tictactoe.collidepoint(event.pos):
                    open_tictactoe()

        SCREEN.blit(background, (0, 0))  # Rysuj tło
        SCREEN.blit(equipment_icon_image, equipment)  # Rysuj ikonę ekwipunku
        SCREEN.blit(tictactoe_icon_image, tictactoe)

        if inv.open:
            inv.draw(SCREEN)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()