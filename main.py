import pygame
import sys


from templates.inventory import Inventory

pygame.init()

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
icon_image = pygame.image.load("assets/equipment.jpg").convert_alpha()
icon_image = pygame.transform.scale(icon_image, (100, 100))
icon_rect = icon_image.get_rect(topleft=(10, 10))

# Skala ikon
icon_size = (100, 100)





def handle_click():
    mouse_pos = pygame.mouse.get_pos()


def main():
    clock = pygame.time.Clock()
    inv = Inventory()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_click()


        #otwieranie ekwipunku
            if event.type == pygame.MOUSEBUTTONDOWN:
                if icon_rect.collidepoint(event.pos):
                    inv.toggle()

        SCREEN.blit(background, (0, 0))  # Rysuj tło
        SCREEN.blit(icon_image, icon_rect)  # Rysuj ikonę ekwipunku

        if inv.open:
            inv.draw(SCREEN)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()